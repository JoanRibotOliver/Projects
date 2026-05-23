import numpy as np
from sys import exit

from decimal import getcontext as ctx, Decimal as D, ROUND_HALF_UP
ctx().rounding = ROUND_HALF_UP

def EDA_NR(n, δn, formatted = True, experimental = False):
    def round05(n, p, five):  # n = number string, p = precition
        if five: k = D(10**(p-1)/5); return ((k*D(n)).quantize(D("0.1"))/k).quantize(D("1." + "0"*p))   # Black magic
        else: return D(n).quantize(D("1." + "0"*p))

    def UncertaintyRounder(δn):
        # Find first non_zero digit
        for i in range(len(δn)):
            if δn[i] not in '0.': firstd = δn[i]; firstd_place = i; break
            if i == len(δn)-1: return "0"  # 0.000... exeption
    
        # Find dot
        if '.' in δn: dot = δn.find('.')
        else: dot = len(δn)
    
        # Rounding parameters
        if firstd == '1': extradecimal = True; five = False
        elif firstd == '2': extradecimal = True; five = True
        else: extradecimal = False; five = False
        
        # Actuall rounding
        if (extradecimal) and (dot == 1): e = q = 1
        elif extradecimal: e = 1; q = 0
        else: e = q = 0
        
        if firstd_place > dot: δn_rounded = round05(δn, firstd_place - dot + e, five)                   # If the number is purely decimal we round using round05.
        else: δn_rounded = ((10**dot)*round05(D(δn)/(10**dot), 1 + e, five)).quantize(D("1." + "0"*q))  # If it is not, then we make it decimal through shifting by a power of 10, round it, unshift it and finally remove extra decimals.
    
        # Remove extra zero when coming from a >= 275 and ending up with 30
        if "." in str(δn_rounded):
            if "3.0" in str(δn_rounded): δn_rounded = D(str(δn_rounded).replace(".0", ""))
            elif "30" in str(δn_rounded).split(".")[1]: δn_rounded = D(str(δn_rounded)[:-1])
            
        return δn_rounded

    def ValueRounder(n, δn_rounded):
        # Geting the decimal places of the rounded error (-power of the least significat figure if not decimal)
        decimal_places = -(δn_rounded.as_tuple().exponent)
        if decimal_places == 0:
            q = 0 if any(x in str(δn_rounded).replace(".", "") for x in ["10", "20"]) else 1
            decimal_places = -([x != "0" for x in str(δn_rounded)][::-1].index(True) + q)
        
        # Getting if the error ends in 20 or 25
        if any(x in str(δn_rounded).replace(".", "") for x in ["20", "25"]): five = True
        else: five = False
        
        # Actuall rounding
        if decimal_places < 0: k = 10**abs(decimal_places); n_rounded = (k*round05(D(n)/k, 1, five)).quantize(D("1"))
        else: n_rounded = round05(n, decimal_places, five)
    
        return n_rounded

    ## If δn = 0, return n ± 0
    if δn == 0 and formatted: return (str(n) + " ± 0")
    elif δn == 0 and not formatted: return (str(n), "0")
    
    ## Change to strings
    try: n, δn = np.format_float_positional(n), np.format_float_positional(δn)
    except: print("ERROR: Can't Round Input"); exit()

    ## Rounding Uncertainty
    δn_rounded = UncertaintyRounder(δn)
    
    ## If experimental = True, remove extra 0s from uncertainty
    if experimental and '.' in str(δn_rounded) and str(δn_rounded)[-1] == '0': δn_rounded = D(str(δn_rounded)[:-1])
        
    ## Rounding Value
    n_rounded = ValueRounder(n, δn_rounded)

    ## Return
    lower_trigger, upper_trigger = -5, 5; common_trigger = abs(min([lower_trigger, upper_trigger])) - 1
    norder = n_rounded.adjusted(); δnorder = δn_rounded.adjusted()
    n_sci = norder <= lower_trigger or norder >= upper_trigger
    δn_sci = δnorder <= lower_trigger or δnorder >= upper_trigger
    ok_distance = abs(norder - δnorder) <= common_trigger
    
    def exponent(norder): return "E" + ("+" if norder > 0 else "") + f"{norder}"
    def δn_rounded_to_sci(δn_rounded):
        temp = f'{δn_rounded:.1E}'
        firstdigit = temp[0] if temp[0] != '-' else temp[1]
        if int(firstdigit) >= 3: temp = temp.replace('.0', '')
        return temp
    
    if str(n_rounded).replace('-', '') == '0' and δn_sci:
        n_rounded, δn_rounded = str(n_rounded), δn_rounded_to_sci(δn_rounded)
        if formatted: return "(" + n_rounded + " ± " + δn_rounded.replace('E', ')E')
        else: return (n_rounded, δn_rounded)
    elif n_sci and ok_distance:
        n_rounded, δn_rounded = EDA_NR(np.float64(n_rounded)/10**norder, np.float64(δn_rounded)/10**norder, formatted = False, experimental = experimental)
        if formatted: return "(" + n_rounded + " ± " + δn_rounded + ")" + exponent(norder)
        else: return (n_rounded + exponent(norder), δn_rounded + exponent(norder))
    else:
        n_rounded = f"{n_rounded:E}" if n_sci else str(n_rounded)
        δn_rounded = δn_rounded_to_sci(δn_rounded) if δn_sci else str(δn_rounded)
        if formatted: return (n_rounded + " ± " + δn_rounded)
        else: return (n_rounded, δn_rounded)

## List / Array rounder
def array_rounder(n, δn): return [EDA_NR(a, b) for a, b in zip(n, δn)]

## Uncertainties module rounders
# --------------------------------------------------------------------------------------------------------
def ufloat_rounder(ufloat, formatted = True, experimental = False):
    return EDA_NR(ufloat.n, ufloat.s, formatted = formatted, experimental = experimental)

def uarray_rounder(uarray, which = 'both', formatted = True, experimental = False):
    L = []; formatted = False if which in ['n', 's'] else formatted
    def appender(rounded_num):
        if which in ['n', 's']: L.append(rounded_num[0 if which == 'n' else 1])
        else: L.append(rounded_num)
    
    for num in uarray: appender(ufloat_rounder(num, formatted = formatted, experimental = experimental))
    return L

def uarray_average(uarray, formatted = True):
    avg = np.sum(uarray)/len(uarray)
    if formatted: return ufloat_rounder(avg)
    else: return avg
# --------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    from uncertainties import ufloat, unumpy
    print(ufloat_rounder(ufloat(2,3)))
    print(uarray_rounder(unumpy.uarray([1,2,3], [0.1, 0.2, 0.3])))
    
    import random as rnd
    for _ in range(10):
        rn = np.float64(rnd.choice([1, -1]) * rnd.random() * 10**rnd.randrange(-12,12,1))
        rδn = np.float64(rnd.random() * 10**rnd.randrange(-12,12,1))
        inset = np.format_float_positional(rn) + " ± " + np.format_float_positional(rδn); print(inset)
        outset = EDA_NR(rn, rδn); print(outset)
        print()