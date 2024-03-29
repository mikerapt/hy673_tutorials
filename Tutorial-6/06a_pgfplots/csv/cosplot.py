import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Define x axis:
r1, r2 = 0, 2*np.pi
theta = np.arange(start=r1, stop=r2, step=0.01)

# Define f(x):
costh = np.cos(theta)
expcosth = np.exp(costh)
line = np.zeros(theta.shape)

# Keep ""global"" min and max of all:
print(f"minx = {r1}, maxx = {r2}")
# minx = 0, maxx = 6.283185307179586
miny, maxy = np.min([costh, expcosth, line]), np.max([costh, expcosth, line])
print(f"miny = {miny}, maxy = {maxy}")
# miny = -0.9991351502732795, maxy = 2.718281828459045

# See how it looks like with Pyplot:
plt.figure()
plt.plot(theta, costh)
plt.plot(theta, expcosth)
plt.plot(theta, line)
plt.show()
plt.close()

# Save as .csv files for PGFPlots:
df1 = pd.DataFrame({'x': theta, 'y': costh})
df2 = pd.DataFrame({'x': theta, 'y': expcosth})
df3 = pd.DataFrame({'x': theta, 'y': line})

df1.to_csv('costh.csv', index=False)
df2.to_csv('expcosth.csv', index=False)
df3.to_csv('line.csv', index=False)
