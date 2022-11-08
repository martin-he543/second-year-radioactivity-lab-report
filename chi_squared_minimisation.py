#%% TASK 19

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import uncertainties as unc
import itertools as iter
from scipy.optimize import curve_fit
from scipy import integrate

# Font Formatting Styles
titleFont = {'fontname': 'Kinnari', 'size': 13}
axesFont = {'fontname': 'Kinnari', 'size': 9}
ticksFont = {'fontname': 'SF Mono', 'size': 7}
errorStyle = {'mew': 1, 'ms': 3, 'capsize': 3, 'color': 'blue', 'ls': ''}
pointStyle = {'mew': 1, 'ms': 3, 'color': 'blue'}
lineStyle = {'linewidth': 0.5}
lineStyleBold = {'linewidth': 1}
histStyle = {'facecolor': 'green', 'alpha': 0.5, 'edgecolor': 'black'}

x19,count19,time,y19,countErr19,yErr19 = \
    np.loadtxt("Task 19 Al.csv",unpack=True,delimiter=",",skiprows=1)

plt.plot(x19,y19,'x')
plt.errorbar(x=x19,xerr=0.01,y=y19,yerr=yErr19, **errorStyle)
plt.xlabel("Thickness / mm", **axesFont)
plt.ylabel("ln (Count)", **axesFont)
plt.xticks(**ticksFont)
plt.yticks(**ticksFont)
plt.title("Task 19: Range of Decay Particles through Al", **titleFont)
# plt.savefig('Task 16.jpg', dpi=1000)

poly19A,cov_poly19A = np.polyfit(x19[:6],y19[:6],1,cov=True)
x= np.linspace(0,3.5,1000)
plt.plot(x,poly19A[0]*x + poly19A[1])
poly19B,cov_poly19B = np.polyfit(x19[9:17],y19[9:17],1,cov=True)
x= np.linspace(1,6,1000)
plt.plot(x,poly19B[0]*x + poly19B[1],color="red")
poly19C,cov_poly19C = np.polyfit(x19[18:],y19[18:],1,cov=True)
x= np.linspace(3,6,1000)
plt.plot(x,poly19C[0]*x + poly19C[1],color="green")

x_intersection = -(poly19B[1] - poly19A[1])/(poly19B[0] - poly19A[0])
print("first intersection: [",x_intersection,poly19A[0]*x_intersection+poly19A[1],"]")
x_intersection = -(poly19C[1] - poly19B[1])/(poly19C[0] - poly19B[0])
print("second intersection: [",x_intersection,poly19B[0]*x_intersection+poly19B[1],"]")

plt.show()

print("Linear Fit Parameters")
print("m₀ = ",poly19A[0],"+/-",np.sqrt(cov_poly19A[0][0]))
print("c₀ = ",poly19A[1],"+/-",np.sqrt(cov_poly19A[1][1]))
print("m₁ = ",poly19B[0],"+/-",np.sqrt(cov_poly19B[0][0]))
print("c₁ = ",poly19B[1],"+/-",np.sqrt(cov_poly19B[1][1]))
print("m₂ = ",poly19C[0],"+/-",np.sqrt(cov_poly19C[0][0]))
print("c₂ = ",poly19C[1],"+/-",np.sqrt(cov_poly19C[1][1]))

area,unc_area = 1.97e-4, 1.4e-5
def exponential_decay(d,A,mu,k,B):                                                                                 
     return A*area*np.exp(-mu*d+k)/(4*np.pi) + B
params, cov_params = curve_fit(exponential_decay,x19,count19, p0=[555000,1.6,10,10])

x=np.linspace(0,5.2,10000)
plt.plot(x19,count19,'x')
plt.plot(x, params[0]*area*np.exp(-params[1]*x+params[2])/(4*np.pi) + params[3], ls='-')
plt.errorbar(x=x19,xerr=0.01,y=count19,yerr=countErr19, **errorStyle)
plt.xlabel("Thickness / mm", **axesFont)
plt.ylabel("Count, u / s¯¹", **axesFont)
plt.xticks(**ticksFont)
plt.yticks(**ticksFont)
plt.title("Task 19: Range of Decay Particles through Al", **titleFont)

print("\nExponential Fit Parameters")
print("A = ",params[0],"+/-",np.sqrt(cov_params[0][0]))
print("µ = ",params[1],"+/-",np.sqrt(cov_params[1][1]))
print("k = ",params[2],"+/-",np.sqrt(cov_params[2][2]))
print("B = ",params[3],"+/-",np.sqrt(cov_params[3][3]))

##### CHI SQUARED SECTION








 
# %% TASK 20
x20,count20,time,y20,count20Err,yErr20 = \
    np.loadtxt("Task 20 Cu.csv",unpack=True,delimiter=",",skiprows=1)

plt.plot(x20,y20,'x')
plt.errorbar(x=x20,xerr=0.01,y=y20,yerr=yErr20, **errorStyle)
plt.xlabel("Thickness / mm", **axesFont)
plt.ylabel("ln (Count)", **axesFont)
plt.xticks(**ticksFont)
plt.yticks(**ticksFont)
plt.title("Task 20: Range of Decay Particles through Cu", **titleFont)
# plt.savefig('Task 16.jpg', dpi=1000)

poly20A,cov_poly20A = np.polyfit(x20[:8],y20[:8],1,cov=True)
x= np.linspace(0,0.8,1000)
plt.plot(x,poly20A[0]*x + poly20A[1])
poly20B,cov_poly20B = np.polyfit(x20[5:12],y20[5:12],1,cov=True)
x= np.linspace(0.3,1.1,1000)
plt.plot(x,poly20B[0]*x + poly20B[1],color="red")
poly20C,cov_poly20C = np.polyfit(x20[14:],y20[14:],1,cov=True)
x= np.linspace(0.8,1.6,1000)
plt.plot(x,poly20C[0]*x + poly20C[1],color="green")

x_intersection = -(poly20B[1] - poly20A[1])/(poly20B[0] - poly20A[0])
print("first intersection",x_intersection,poly20A[0]*x_intersection+poly20A[1])
x_intersection = -(poly20C[1] - poly20B[1])/(poly20C[0] - poly20B[0])
print("second intersection",x_intersection,poly20B[0]*x_intersection+poly20B[1])

plt.show()

print("Linear Fit Parameters")
print("m₀ = ",poly20A[0],"+/-",np.sqrt(cov_poly20A[0][0]))
print("c₀ = ",poly20A[1],"+/-",np.sqrt(cov_poly20A[1][1]))
print("m₁ = ",poly20B[0],"+/-",np.sqrt(cov_poly20B[0][0]))
print("c₁ = ",poly20B[1],"+/-",np.sqrt(cov_poly20B[1][1]))
print("m₂ = ",poly20C[0],"+/-",np.sqrt(cov_poly20C[0][0]))
print("c₂ = ",poly20C[1],"+/-",np.sqrt(cov_poly20C[1][1]))

area,unc_area = 1.97e-4, 1.4e-5
def exponential_decay(d,A,mu,k,B):                                                                                 
     return A*area*np.exp(-mu*d+k)/(4*np.pi) + B
params, cov_params = curve_fit(exponential_decay,x20,count20)

x=np.linspace(0,1.55,10000)
plt.plot(x20,count20,'x')
plt.plot(x, params[0]*area*np.exp(-params[1]*x+params[2])/(4*np.pi) + params[3], ls='-')
plt.errorbar(x=x20,xerr=0.01,y=count20,yerr=count20Err, **errorStyle)
plt.xlabel("Thickness / mm", **axesFont)
plt.ylabel("Count, u / s¯¹", **axesFont)
plt.xticks(**ticksFont)
plt.yticks(**ticksFont)
plt.title("Task 20: Range of Decay Particles through Cu", **titleFont)

print("\nExponential Fit Parameters")
print("A = ",params[0],"+/-",np.sqrt(cov_params[0][0]))
print("µ = ",params[1],"+/-",np.sqrt(cov_params[1][1]))
print("k = ",params[2],"+/-",np.sqrt(cov_params[2][2]))
print("B = ",params[3],"+/-",np.sqrt(cov_params[3][3]))

##### CHI SQUARED SECTION
