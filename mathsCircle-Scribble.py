import numpy as np

tri_pos = [np.random.randint(-3, 3), np.random.randint(-3, 3), 0]
z = tri_pos[0] + 1j*tri_pos[1]
rotated_z = z * np.exp(1j * np.pi / 2)
tri_pos_rotated = [round(float(rotated_z.real),2), round(float(rotated_z.imag),2), 0]

print("Original:", tri_pos)
print("Rotated: ", tri_pos_rotated)
