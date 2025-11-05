import numpy as np

num_samples = 5000
mean = 0
std_dev = 1
filename = "noise.csv"

noise = np.random.normal(mean, std_dev, num_samples)

np.savetxt(filename, noise, delimiter=",")
print(f"{filename} generated with {num_samples} samples.")
