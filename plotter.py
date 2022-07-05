'''
from matplotlib import pyplot as plt, rcParams
from matplotlib import style
from main import currentfile
import numpy as np

currentfile = "/home/kre8or/PycharmProjects/Stargaze/recordings/today_06222022-155021_device_0.csv"

plt.title('Gaze Angle X for steep left lighting')
plt.ylabel('gaze angle in radians')
plt.xlabel('time in seconds')
x, y = np.loadtxt(currentfile, unpack=True, delimiter=',', usecols=(0, 11),
                  skiprows=1)

plt.scatter(x, y, s=rcParams['lines.markersize'] ** 1.1)
# plt.scatter(m, n)
plt.show()
'''