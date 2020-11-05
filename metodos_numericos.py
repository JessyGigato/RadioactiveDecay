import matplotlib.pyplot as plt
import numpy as np
from numpy import math as m


def exact_sol(k,y0,t):
    return y0 * m.pow(m.e,-k*t)

def values_exact_sol(y0,a,b,h,tm):
    k = m.log(2)/tm
    x_range = np.arange(a,b,h)
    y = []
    for x in x_range:
        yn = exact_sol(k,y0,x)
        y.append(yn)
    return x_range,y

def EDO_dr(xn,yn,k):
    return -k * yn

def euler_method(x0,y0,a,b,h,tm):
    k = m.log(2)/tm
    xn = x0
    yn = y0
    x = [xn]
    y = [yn]
    while xn <= b:
        fn = EDO_dr(xn,yn,k)
        xn = xn + h
        yn = yn + h * fn
        x.append(xn)
        y.append(yn)
    return x,y
    
def runge_kutta_method(x0,y0,a,b,h,tm):
    k = m.log(2)/tm
    xn = x0
    yn = y0
    x = [xn]
    y = [yn]
    while xn <= b:
        k1 = EDO_dr(xn,yn,k)
        k2 = EDO_dr(xn + (1/2) * h,yn +(1/2) * h * k1,k)
        k3 = EDO_dr(xn + (1/2) * h,yn + (1/2) * h * k2,k)
        xn = xn + h
        k4 = EDO_dr(xn,yn + h*k3,k)
        yn = yn + (h/6) * (k1+ 2 * k2 + 2 * k3 + k4)
        x.append(xn)
        y.append(yn)
    return x,y


