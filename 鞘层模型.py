import matplotlib.pyplot as plt
import sys
import numpy as np


# initial condition
ne ,ni , vi, E = 1,1,1,0.01
B ,X =0,0
dx = 0.01
vi0 = vi
initial = [[X ,vi ,ni , E, ne ,B]]

# equation
for i in range(10000):
    X += dx
    vi += E/vi*dx
    ni = vi0/vi
    E += (ni - ne)*dx
    B -= E*dx
    ne = np.exp(B)
    ls = [[X ,vi ,ni , E, ne ,B]]
    initial = np.append(initial, ls, axis=0)


axe = plt.figure(figsize=(5,10))
plt.subplot(211)
plt.plot(initial[:,0],initial[:,2],linewidth = 3,label = 'Ni')
plt.plot(initial[:,0],initial[:,4],linewidth = 3,label = 'Ne')
plt.legend()
plt.subplot(212)
plt.plot(initial[:,0],initial[:,5],linewidth = 3)

plt.show()
