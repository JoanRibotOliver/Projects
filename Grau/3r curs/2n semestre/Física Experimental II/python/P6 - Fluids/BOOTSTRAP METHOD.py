# BOOTSTRAP METHOD

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, a, b, c):
    return - a * np.log(1 + b * x) + c


# Datos de ejemplo:
#x = np.array([0.00000001, 0.08727272727, 0.16, 0.2215384615, 0.2742857143, 0.32, 0.36, 0.3952941176, 0.4266666667, 0.4547368421, 0.48, 0.96, 0.8727272727, 0.80, 0.7384615385, 0.6857142857, 0.64, 0.60, 0.5647058824, 0.5333333333, 0.5052631579, 0.48])
#y = np.array([0.08018493316, 0.06317600794, 0.04130738981, 0.04616708273, 0.04211733863, 0.04130738981, 0.03968749217, 0.03806759453, 0.04049744099, 0.04130738981, 0.04049744099, 0.03239795279, 0.03239795279, 0.03320790161, 0.03482779925, 0.03644769689, 0.03725764571, 0.03725764571, 0.03806759453, 0.03806759453, 0.03887754335, 0.04049744099])

# Dades nostres:
x = np.array([0, 0.087272727, 0.16, 0.221538462, 0.274285714, 0.32, 0.36, 0.395294118, 0.426666667, 0.454736842, 0.48, 1, 0.872727273, 0.8, 0.738461538, 0.685714286, 0.64, 0.6, 0.564705882, 0.533333333, 0.505263158, 0.48])
y = np.array([0.065605854, 0.059126264, 0.051836724, 0.048596929, 0.046977032, 0.045357134, 0.042927287, 0.040497441, 0.04130739, 0.04130739, 0.04130739, 0.032397953, 0.033207902, 0.034827799, 0.036447697, 0.037257646, 0.042117339, 0.042927287, 0.0396874920, 0.040497441, 0.04130739, 0.042117339])


# Función de ajuste con el método bootstrap
def bootstrap_fit(x, y, num_bootstrap=20000):
    n = len(x)
    bootstrap_params = []

    for _ in range(num_bootstrap):
        indices = np.random.choice(n, n, replace=True)
        indices[0] = 0  # Reemplazar el primer índice por 0 para asegurar que pase por el primer punto
        x_bootstrap = x[indices]
        y_bootstrap = y[indices]
        try:
            popt, _ = curve_fit(func, x_bootstrap, y_bootstrap, bounds=([-np.inf, -np.inf, -np.inf], [np.inf, np.inf, np.inf]), p0=[1, 1, 1])
            y_bootstrap_fit = func(x, popt[0], popt[1], popt[2])
            if abs(y_bootstrap_fit[0] - y[0]) < 0.001:
                bootstrap_params.append(popt)
        except RuntimeError:
            pass

    return np.array(bootstrap_params)

bootstrap_params = bootstrap_fit(x, y)

if len(bootstrap_params) > 0:
    median_params = np.median(bootstrap_params, axis=0)
    a_median = median_params[0]
    b_median = median_params[1]

    x_fit = np.linspace(min(x), max(x), 100)
    
    # Errors Miki:
    #x_error=[0, 0.006347107, 0.011333333, 0.015337278, 0.018612245, 0.021333333, 0.023625, 0.025577855, 0.027259259, 0.028720222, 0.03, 0, 0.006743802, 0.012666667, 0.017893491, 0.022530612, 0.026666667, 0.030375, 0.033716263, 0.036740741, 0.039490305, 0.042]
    y_error=0.00080994882

    # Errors nostros:
    #x_error=[0.0096, 0.008727273, 0.008, 0.007384615, 0.006857143, 0.0064, 0.006, 0.005647059, 0.005333333, 0.005052632, 0.0048, 0.01, 0.008727273, 0.008, 0.007384615, 0.006857143, 0.005647059, 0.005333333, 0.005052632, 0.0048]
    #y_error=0.0008099
    x_error=x/100

    for i in range(len(bootstrap_params)):
        popt = bootstrap_params[i]
        y_bootstrap_fit = func(x_fit, popt[0], popt[1], popt[2])
        plt.plot(x_fit, y_bootstrap_fit, color='gray', alpha=0.2)

    plt.errorbar(x, y, xerr=x_error, yerr=y_error, color='blue', label='Dades', capsize=3, markersize=4, fmt='o')
    plt.xlabel('c (v/v)')
    plt.ylabel('σ (N/m)')
    plt.title('Tensió superficial vs Concentración en volum')
    plt.legend()
    plt.show()

    print("Valor d'a:", a_median)
    print("Valor de b:", b_median)
    
    # Histogramas de las constantes
    fig, axs = plt.subplots(1, 2, figsize=(12, 4))


    a_values = bootstrap_params[:, 0]
    b_values = bootstrap_params[:, 1]

    axs[0].hist(a_values, bins=30, edgecolor='black', color='green')
    axs[0].set_title("Distribució d'α")
    axs[0].set_xlabel('α (N/m)')
    axs[0].set_ylabel('Freqüència')

    axs[1].hist(b_values, bins=30, edgecolor='black', color='green')
    axs[1].set_title('Distribució de β')
    axs[1].set_xlabel('β')
    axs[1].set_ylabel('Freqüència')

    

    plt.tight_layout()
    plt.show()

    # Cálculo de intervalos de confianza (cuantiles 17-83)
    a_interval = np.percentile(a_values, [17, 83])
    b_interval = np.percentile(b_values, [17, 83])

    print("Interval de confiança per a (quantiles 17-83):", a_interval)
    print("Interval de confiança per b (quantiles 17-83):", b_interval)
else:
    print("No s'han trobat solucions vàlides amb el mètode bootstrap.")