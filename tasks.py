import numpy as np
import matplotlib.pyplot as plt

titleFont = {'fontname': 'Times New Roman', 'size': 13}
axesFont = {'fontname': 'Times New Roman', 'size': 11}
ticksFont = {'fontname': 'SF Mono', 'size': 7}
errorStyle = {'mew': 1, 'ms': 3, 'capsize': 3, 'color': 'blue', 'ls': ''}
pointStyle = {'mew': 1, 'ms': 3, 'color': 'blue'}
lineStyle = {'linewidth': 0.5}
lineStyleBold = {'linewidth': 1}
histStyle = {'facecolor': 'green', 'alpha': 0.5, 'edgecolor': 'black'}


#%% TASK 6
# ______________________________________________

E_deposited, SourceZ, SIAngleOffAxis, AbsorberThickeness = \
    np.loadtxt(r"H:\Lab\6_data.txt",skiprows=1,unpack=True,delimiter=",")

plt.hist(E_deposited,bins=25)
plt.xlabel("Energy Deposited in SI", **axesFont)
plt.ylabel("Number of Particles", **axesFont)
plt.xticks(**ticksFont)
plt.yticks(**ticksFont)
plt.title("Task 6: Histogram of Particle Simulation", **titleFont)
plt.savefig('Task 6 25 bins.jpg', dpi=1000)
plt.show()


#%% TASK 7
# ______________________________________________

E_deposited300, SourceZ, SIAngleOffAxis, AbsorberThickeness = \
    np.loadtxt(r"H:\Lab\7_data_0.3MeVOllie.txt",skiprows=1,unpack=True,delimiter=",")

E_deposited2000, SourceZ, SIAngleOffAxis, AbsorberThickeness = \
    np.loadtxt(r"H:\Lab\7_data_2MeV.txt",skiprows=1,unpack=True,delimiter=",")

plt.hist(E_deposited300,bins=50)
plt.xlabel("Energy Deposited in SI", **axesFont)
plt.ylabel("Number of Particles", **axesFont)
plt.xticks(**ticksFont)
plt.yticks(**ticksFont)
plt.title("Task 7: Histogram of Energy Deposited by 300KeV Electrons", **titleFont)
plt.savefig('Task 7 0.3MeV.jpg', dpi=1000)
plt.show()

plt.hist(E_deposited2000,bins=50)
plt.xlabel("Energy Deposited in SI", **axesFont)
plt.ylabel("Number of Particles", **axesFont)
plt.xticks(**ticksFont)
plt.yticks(**ticksFont)
plt.title("Task 7: Histogram of Energy Deposited by 2MeV Electrons", **titleFont)
plt.savefig('Task 7 2MeV.jpg', dpi=1000)
plt.show()

#%% TASK 8
# ______________________________________________

E_deposited60, SourceZ, SIAngleOffAxis, AbsorberThickeness = \
    np.loadtxt(r"H:\Lab\8_data_0.06MeV_new.txt",skiprows=1,unpack=True,delimiter=",")

E_deposited2000, SourceZ, SIAngleOffAxis, AbsorberThickeness = \
    np.loadtxt(r"H:\Lab\8_data_2MeV_new.txt",skiprows=1,unpack=True,delimiter=",")

plt.hist(E_deposited60,bins=50)
plt.xlabel("Energy Deposited in SI", **axesFont)
plt.ylabel("Number of Particles", **axesFont)
plt.xticks(**ticksFont)
plt.yticks(**ticksFont)
plt.title("Task 8: Histogram of Energy Deposited by 60KeV Gamma Rays", **titleFont)
plt.savefig('Task 8 0.06MeV.jpg', dpi=1000)
plt.show()

plt.hist(E_deposited2000,bins=50)
plt.xlabel("Energy Deposited in SI", **axesFont)
plt.ylabel("Number of Particles", **axesFont)
plt.xticks(**ticksFont)
plt.yticks(**ticksFont)
plt.title("Task 8: Histogram of Energy Deposited by 2MeV Gamma Rays", **titleFont)
plt.savefig('Task 8 2MeV.jpg', dpi=1000)
plt.show()


#%% TASK 9
# ______________________________________________



#%% TASK 10
# ______________________________________________