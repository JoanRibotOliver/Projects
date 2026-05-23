"""
Created on Tue Dec 27 17:19:22 2022

@author: joanribot
"""


# =============================================================================
# =============================================================================
# PRÀCTICA 3, APARTATS D) I E)
# =============================================================================
# =============================================================================

import matplotlib.pyplot as plt
import math

Jlist = [11,21,41,81,161]

# =============================================================================
# Perfil a
# =============================================================================

Ea1 = [0.02436, 0.006174, 0.001541, 0.000387, 0.00009686]
Ea2 = [0.01815,	0.009416,	0.004756,	0.002414,	0.001218]
Ea3 = [0.01032,	0.009416,	0.007897,	0.005943,	0.003987]
Ea4 = [0.1127,	0.03034,	0.01658,	0.008393,	0.004265]
Ea5 = [0.04179,	0.03034,	0.01878,	0.01053,	0.005503]
Ea6 = [0.06194,	0.03734,	0.01963,	0.009893,	0.005038]
Ea7 = [0.05921,	0.03734,	0.02109,	0.01120,	0.005680]

Ta1 = [7.073, 54.870, 442.303, 3161.622, 25109.167]
Ta2 = [7.353, 53.945, 412.698, 3336.997,24933.227]
Ta3 = [14.313, 58.982, 202.970, 786.221, 3155.491]
Ta4 = [0.780, 5.442, 40.803, 317,521, 2497.237]
Ta5 = [1.454, 5.513, 20.919, 82,554, 326.744]
Ta6 = [0.801, 5.321, 41.438, 318,228, 2638.136]
Ta7 = [1.399, 5.392, 21.113, 81,134, 353.552]

Ea1log = []
Ea2log = []
Ea3log = []
Ea4log = []
Ea5log = []
Ea6log = []
Ea7log = []

Ta1log = []
Ta2log = []
Ta3log = []
Ta4log = []
Ta5log = []
Ta6log = []
Ta7log = []

for i in range(5):
    Ea1log.append(math.log(Ea1[i],10))
    Ea2log.append(math.log(Ea2[i],10))
    Ea3log.append(math.log(Ea3[i],10))
    Ea4log.append(math.log(Ea4[i],10))
    Ea5log.append(math.log(Ea5[i],10))
    Ea6log.append(math.log(Ea6[i],10))
    Ea7log.append(math.log(Ea7[i],10))
    Ta1log.append(math.log(Ta1[i],10))
    Ta2log.append(math.log(Ta2[i],10))
    Ta3log.append(math.log(Ta3[i],10))
    Ta4log.append(math.log(Ta4[i],10))
    Ta5log.append(math.log(Ta5[i],10))
    Ta6log.append(math.log(Ta6[i],10))
    Ta7log.append(math.log(Ta7[i],10))

plt.plot(Jlist,Ea1log,"r.-",label="θ = 0, v = 0.5")
plt.plot(Jlist,Ea2log,"b.-",label="θ = 0.5, v = 0.5")
plt.plot(Jlist,Ea3log,"y.-",label="θ = 0.5, μ = 0.025")
plt.plot(Jlist,Ea4log,"g.-",label="θ = 0.5, v = 5")
plt.plot(Jlist,Ea5log,"c.-",label="θ = 0.5, μ = 0.25")
plt.plot(Jlist,Ea6log,"m.-",label="θ = 1, v = 5")
plt.plot(Jlist,Ea7log,"k.-",label="θ = 1, μ = 0.25")

plt.xlabel("J"), plt.ylabel("log(E)")

plt.title("Perfil a. log(E) Vs. J")
plt.legend(loc='best', facecolor="w", fontsize=9)
plt.grid()
plt.show()

plt.plot(Ta1log,Ea1,"r.-",label="θ = 0, v = 0.5")
plt.plot(Ta2log,Ea2,"b.-",label="θ = 0.5, v = 0.5")
plt.plot(Ta3log,Ea3,"y.-",label="θ = 0.5, μ = 0.025")
plt.plot(Ta4log,Ea4,"g.-",label="θ = 0.5, v = 5")
plt.plot(Ta5log,Ea5,"c-",label="θ = 0.5, μ = 0.25")
plt.plot(Ta6log,Ea6,"m.-",label="θ = 1, v = 5")
plt.plot(Ta7log,Ea7,"k.-",label="θ = 1, μ = 0.25")

plt.xlabel("log(T[s])"), plt.ylabel("E")

plt.title("Perfil a")
plt.legend(loc='best', facecolor="w", fontsize=10)
plt.grid()
plt.show()

# =============================================================================
# Perfil b
# =============================================================================

Eb1 = [0.07036,	0.04362,	0.02410,	0.01263,	0.006454]
Eb2 = [0.01995,	0.03065,	0.01624,	0.008359,	0.004237]
Eb3 = [0.01136,	0.03065,	0.01791,	0.01570,	0.006104]
Eb4 = [0.1900,	0.05427,	0.01963,	0.01112,	0.006209]
Eb5 = [0.04209,	0.05427,	0.04734,	0.04277,	0.03888]
Eb6 = [0.06556,	0.04452,	0.02521,	0.01361,	0.007112]
Eb7 = [0.06342,	0.04452,	0.02434,	0.01281,	0.006574]

Eb1log = []
Eb2log = []
Eb3log = []
Eb4log = []
Eb5log = []
Eb6log = []
Eb7log = []

Tb1 = [6.766, 49.582, 383.794, 2906.716, 23707.434]
Tb2 = [6.672, 50,141, 383.336, 2997.923, 23627.845]
Tb3 = [13.341, 50.521, 190.317, 743.792, 2940.613]
Tb4 = [0.750, 5.005, 38.366, 306.849, 2361.947]
Tb5 = [1.339, 5.065, 19.298, 75.101, 295.893]
Tb6 = [0.838, 6.123, 40.470, 302.828, 2477.468]
Tb7 = [1.287, 5.172, 19.579, 75.823, 294.072]

Tb1log = []
Tb2log = []
Tb3log = []
Tb4log = []
Tb5log = []
Tb6log = []
Tb7log = []

for i in range(5):
    Eb1log.append(math.log(Eb1[i],10))
    Eb2log.append(math.log(Eb2[i],10))
    Eb3log.append(math.log(Eb3[i],10))
    Eb4log.append(math.log(Eb4[i],10))
    Eb5log.append(math.log(Eb5[i],10))
    Eb6log.append(math.log(Eb6[i],10))
    Eb7log.append(math.log(Eb7[i],10))
    Tb1log.append(math.log(Tb1[i],10))
    Tb2log.append(math.log(Tb2[i],10))
    Tb3log.append(math.log(Tb3[i],10))
    Tb4log.append(math.log(Tb4[i],10))
    Tb5log.append(math.log(Tb5[i],10))
    Tb6log.append(math.log(Tb6[i],10))
    Tb7log.append(math.log(Tb7[i],10))

plt.plot(Jlist,Eb1log,"r.-",label="θ = 0, v = 0.5")
plt.plot(Jlist,Eb2log,"b.-",label="θ = 0.5, v = 0.5")
plt.plot(Jlist,Eb3log,"y.-",label="θ = 0.5, μ = 0.025")
plt.plot(Jlist,Eb4log,"g.-",label="θ = 0.5, v = 5")
plt.plot(Jlist,Eb5log,"c.-",label="θ = 0.5, μ = 0.25")
plt.plot(Jlist,Eb6log,"m.-",label="θ = 1, v = 5")
plt.plot(Jlist,Eb7log,"k.-",label="θ = 1, μ = 0.25")

plt.xlabel("J"), plt.ylabel("log(E)")

plt.title("Perfil b. log(E) Vs. J")
plt.legend(loc='best', facecolor="w", fontsize=9)
plt.grid()
plt.show()

plt.plot(Tb1log,Eb1,"r.-",label="θ = 0, v = 0.5")
plt.plot(Tb2log,Eb2,"b.-",label="θ = 0.5, v = 0.5")
plt.plot(Tb3log,Eb3,"y.-",label="θ = 0.5, μ = 0.025")
plt.plot(Tb4log,Eb4,"g.-",label="θ = 0.5, v = 5")
plt.plot(Tb5log,Eb5,"c-",label="θ = 0.5, μ = 0.25")
plt.plot(Tb6log,Eb6,"m.-",label="θ = 1, v = 5")
plt.plot(Tb7log,Eb7,"k.-",label="θ = 1, μ = 0.25")

plt.xlabel("log(T[s])"), plt.ylabel("E")

plt.title("Perfil b")
plt.legend(loc='best', facecolor="w", fontsize=10)
plt.grid()
plt.show()
