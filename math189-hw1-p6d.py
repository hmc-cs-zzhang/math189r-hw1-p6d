import numpy
import matplotlib.pyplot as plt

mean = 0
std = 1
num_samples = 100

# Generate white noise
noise = numpy.random.normal(mean, std, size=num_samples)

xstart = 0
xend = 100
sample_m = 62.0 / 35.0
sample_b = 18.0 / 35.0

# Generate 100 points near the line
sample_x = numpy.linspace(xstart, xend, num=num_samples)
sample_y = []
for i in range(num_samples):
	sample_y.append(sample_m * sample_x[i] + sample_b + noise[i])

# Find m and b that fit the points
A = numpy.matrix([[x, 1] for x in sample_x])
At = A.transpose()

result = numpy.linalg.inv(At * A) * At * numpy.matrix(sample_y).transpose()
new_m = result.item(0)
new_b = result.item(1)
print new_m, new_b

plt.plot(sample_x, sample_y, 'ro')
plt.plot(sample_x, sample_x * sample_m + sample_b)
plt.plot(sample_x, sample_x * new_m + new_b)
plt.show()
