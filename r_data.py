import csv
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

with open('4data.csv', 'r') as f:
  reader = csv.reader(f)
  your_list = list(reader)

print(your_list)
xs = []
ys = []
zs = []
for i in range(len(your_list)):
    for j in range(len(your_list[i])):
        if your_list[i][j]!='0':
            xs.append(i)
            ys.append(j)
            zs.append(your_list[i][j])
        
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

n = 100
xs = np.array(xs, dtype=np.float64)
ys = np.array(ys, dtype=np.float64)
zs = np.array(zs, dtype=np.float64)
ax.scatter(xs, ys, zs, c='r', marker='o')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_zlim([0, 250])
plt.show()
    
