import numpy
import matplotlib.pyplot as plt

sample_m = 62.0 / 35.0
sample_b = 18.0 / 35.0

sample_x = numpy.arange(6)
plt.plot(sample_x, sample_x * sample_m + sample_b)
plt.plot([0, 2, 3, 4], [1, 3, 6, 8], 'ro')
plt.show()