import matplotlib.pyplot as plt
import numpy as np

import matplotlib
matplotlib.use("TkAgg")

#PV = nRT
#n = N/N_A
# -> P = nRT/V

#CONSTANTS
N = 100             #n
container = 10      #V
T = 1000
speed = 0.1         # kinda T

#INIT
positions = np.random.rand(N, 2) * container
velocities = np.random.rand(N, 2) * speed

#Figure
fig, ax = plt.subplots()
scatter = ax.scatter(positions[:, 0], positions[:, 1], marker='o')
ax.set_xlim(0, container)
ax.set_ylim(0, container)
plt.gca().set_aspect("equal", adjustable="box")

#Simulation
collisions_arr = []
for step in range(T):
    positions += velocities
    num_collisions = 0

    for i in range(N):
        for j in range(2):
            if positions[i,j] < 0 or positions[i, j] > container:
                #collides
                velocities[i,j] *= -1
                num_collisions += 1

    collisions_arr = np.append(collisions_arr, num_collisions)

    print(f"{step}: No collisions: {num_collisions} - Average: {np.average(collisions_arr):.2f}", end='\r')
    
    if not plt.fignum_exists(fig.number):
        break

    scatter.set_offsets(positions)
    plt.pause(0.001)

plt.show()