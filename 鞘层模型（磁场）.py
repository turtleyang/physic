import matplotlib.pyplot as plt
import sys
import numpy as np


# initial condition
ni ,ne ,E, k ,x ,phi ,dx= 1,1,0.01,np.pi/2,0,0,0.01
B = 5
vx,vy,vz =1,0.1,0
vx0 = vx

y,z =0,0
Bx,Bz = np.cos(k),np.sin(k)
initial = [[x ,vx ,ni , E, ne ,phi,y,z]]

# equation
for i in range(10000):

    ni = vx0/vx
    ne = np.exp(phi)
    phi -= E*dx
    E += (ni-ne)*dx
    vx += (E+B*vy*Bz)/vx*dx
    vy += B*(vz*Bx-vx*Bz)/vx*dx
    vz -= B*vy*Bx/vx*dx
    x += dx
    ls = [[x ,vx ,ni , E, ne , phi, vy ,vz]]
    initial = np.append(initial, ls, axis=0)


axe = plt.figure(figsize=(5,10))
print(np.shape(initial))
plt.subplot(211)
plt.plot(initial[:,0],initial[:,2],linewidth = 3,label = 'Ni')
plt.plot(initial[:,0],initial[:,4],linewidth = 3,label = 'Ne')
plt.legend()
plt.subplot(212)
plt.plot(initial[:,0],initial[:,5],linewidth = 3)

axe1 = plt.figure(figsize=(5,10))
print(np.shape(initial))
plt.subplot(211)
plt.plot(initial[:,0],initial[:,1],linewidth = 3,label = 'Ni')

ax = plt.figure().add_subplot(projection='3d')
ax.plot(initial[:, 1], initial[:, 6], initial[:, 7], label='parametric curve')
plt.xlabel('x')
plt.ylabel('y')
plt.clabel('z')
ax.legend()

plt.show()
