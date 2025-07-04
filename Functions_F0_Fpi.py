''' This script contains F0, Fpi, and their derivatives. 
These functions are important for the bi-modal non-uniform field.'''
import numpy as np
import scipy
i0 = np.i0
i1 = scipy.special.i1
iv = scipy.special.iv

def F0(r,theta,h,p):
    chance = np.array([p,1-p])
    eta = np.array([1,-1])
    F0 = 0
    for i in range(0,2):
        x = 2* (theta * r + h * eta[i])
        F0 += chance[i]*(i1(x) / i0(x))
    return F0

def F0der(r,theta,h,p):
    chance = np.array([p,1-p])
    eta = np.array([1,-1])
    F0der = 0
    for i in range(0,2):
        x = 2* (theta * r + h * eta[i])
        F0der += chance[i]*(2 * theta * (1/2 + 1/2 * iv(2,x) / i0(x) - (i1(x)/i0(x))**2))
    return F0der

def F0der2(r,theta,h,p):
    chance = np.array([p,1-p])
    eta = np.array([1,-1])
    F0der2 = 0
    for i in range(0,2):
        x = 2* (theta * r + h * eta[i])
        I0 = i0(x)
        I1 = i1(x)
        I2 = iv(2,x)
        I3 = iv(3,x)
        F0der2 += chance[i]*(4 * theta**2* (1/I0 * (I3/4 - 3*I1/4) - 3/2 * I1*I2 / I0**2 + 2 * I1**3 / I0**3))
    return F0der2

def F0der3(r,theta,h,p):
    chance = np.array([p,1-p])
    eta = np.array([1,-1])
    F0der3 = 0
    for i in range(0,2):
        x = 2* (theta * r + h * eta[i])
        I0 = i0(x)
        I1 = i1(x)
        I2 = iv(2,x)
        I3 = iv(3,x)
        I4 = iv(4,x)
        term0 = -3/8
        term1 = (-I2 + I4/8)
        term2 = -I1*I3 - 3 / 4 * I2**2 + 3 * I1**2
        term3 = 6 * I1**2 * I2
        term4 = -6*I1**4
        F0der3 += chance[i]*(8*theta**3*(term0 + term1/I0 + term2/I0**2 + term3/I0**3 + term4/I0**4))
    return F0der3

def Fpi(r,theta,h,p):
    chance = np.array([p,1-p])
    eta = np.array([1,-1])
    Fpi = 0
    for i in range(0,2):
        x = 2* (theta * r - h * eta[i])
        Fpi += chance[i]*(i1(x) / i0(x))
    return Fpi

def Fpider(r,theta,h,p):
    chance = np.array([p,1-p])
    eta = np.array([1,-1])
    Fpider = 0
    for i in range(0,2):
        x = 2* (theta * r - h * eta[i])
        Fpider += chance[i]*(2 * theta * (1/2 + 1/2 * iv(2,x) / i0(x) - (i1(x)/i0(x))**2))
    return Fpider

def Fpider2(r,theta,h,p):
    chance = np.array([p,1-p])
    eta = np.array([1,-1])
    Fpider2 = 0
    for i in range(0,2):
        x = 2* (theta * r - h * eta[i])
        I0 = i0(x)
        I1 = i1(x)
        I2 = iv(2,x)
        I3 = iv(3,x)
        Fpider2 += chance[i]*(4 * theta**2* (1/I0 * (I3/4 - 3*I1/4) - 3/2 * I1*I2 / I0**2 + 2 * I1**3 / I0**3))
    return Fpider2

def Fpider3(r,theta,h,p):
    chance = np.array([p,1-p])
    eta = np.array([1,-1])
    Fpider3 = 0
    for i in range(0,2):
        x = 2* (theta * r - h * eta[i])
        I0 = i0(x)
        I1 = i1(x)
        I2 = iv(2,x)
        I3 = iv(3,x)
        I4 = iv(4,x)
        term0 = -3/8
        term1 = (-I2 + I4/8)
        term2 = -I1*I3 - 3 / 4 * I2**2 + 3 * I1**2
        term3 = 6 * I1**2 * I2
        term4 = -6*I1**4
        Fpider3 += chance[i]*(8*theta**3*(term0 + term1/I0 + term2/I0**2 + term3/I0**3 + term4/I0**4))
    return Fpider3






