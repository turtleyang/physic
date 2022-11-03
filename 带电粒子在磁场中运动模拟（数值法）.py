import matplotlib.pyplot as plt
import sys
import numpy as np

# 给定初始条件
vx, vy, vz = 0, 1, 1  # 速度分量
x, y, z = 0, 0, 0  # 位置
t = 0
h = 0.1  # 步长
q, b, e, m = 0.0016, 1, 0.001, 0.02
initial = [[0, 0, 0, 0, 0, 0, 0]]

# 差分法求解方程
for i in range(10000):
    vx += q * b * vy / m * h
    vy += (q * e / m - q * b * vx / m) * h
    x += vx * h
    y += vy * h
    z += vz * h
    t += h
    ls = [[t, x, y, z, vx, vy, vz]]
    initial = np.append(initial, [[t, x, y, z, vx, vy, vz]], axis=0)

ax = plt.figure().add_subplot(projection='3d')
ax.plot(initial[:, 1], initial[:, 2], initial[:, 3], label='parametric curve')
plt.xlabel('x')
plt.ylabel('y')
plt.clabel('z')
ax.legend()

plt.show()

