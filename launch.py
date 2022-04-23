from typing import IO
import numpy as np
import math
import matplotlib.pyplot as plt
from fireflyalgorithm.thermal_coefficients import getA, getB, getC
from fireflyalgorithm.fireflyalgorithm import FireflyAlgorithm
FA = FireflyAlgorithm()
def getSolar(x):
    # J = ((Rb + p(1-math.cos(B))/2) + (-Rb +(1+math.cos(B))/2))
    # Jd= (-Rb +(1+math.cos(B))/2)*q*Io
    
    # if(J>0 and Jd<0):
    #     f = (k(K - 0.5(x+tow))/tow)e**(lamda * (x+tow)/2)
    # if J>0 and Jd>0:
    #     alp = x/tow
    #     (k(K - 0.5(x+tow))/tow)
    return 0
def getWind(x,Vr):
    sh=2.39
    sc=37.7
    vi=3.5
    l=3.28
    Vo =25.0
    e =2.718
    c=4.89
    pl=1.0
    f=0.0
    if(x<Vr):
        f= ((sh*vi*l/sc)*((1+pl)*vi/sc)**(sh-1))*e**(-(1+pl)*vi/sc)**sh
    if(x==0.0):
        f= 1 - e**((-Vr/sc)**sh) + e**((-Vo/sc)**sh)
    if(x==Vr):
        f= e**((-Vr/sc)**sh) - e**((-Vo/sc)**sh)

    return c*f
def getThermal(x): 
    return getA()*(x**2) + getB()*x +getC()
def f(x):
    sm=0
    for i in x:
        sm+=(getSolar(i) + getWind(i,15.0) + getThermal(i))
    return sm
    #return np.sum(x**2 +x +1)
#3 unit system
data = [
    # an         bn     cn   Pmin,Pmax
    [1243.5311, 38.30553,0.03, 35 , 210],
    [1658.56, 36.32, 0.0211,   130, 325],
    [1356.65,38.27    ,0.017,  125,315]
]
for d in data:
    an=d[0]
    bn=d[1]
    cn=d[2]
    Pmin=d[3]
    Pmax=d[4]
    FA = FireflyAlgorithm(10,an,bn,cn)
    op=FA.run(function=f, dim=1, lb=Pmin, ub=Pmax, max_evals=100000)
    print((op))
# arr = FA.run(function=f, dim=10, lb=-5, ub=5, max_evals=10000)
# plt.plot(arr)
# plt.show()
# print(arr)