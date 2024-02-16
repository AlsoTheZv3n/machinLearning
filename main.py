import numpy
from scipy import stats
import matplotlib.pyplot as plt

# Mean - The average value
# The median value is the value in the middle, after you have sorted all the values:
# 77, 78, 85, 86, 86, 86, 87, 87, 88, 94, 99, 103, 111
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

print("Mean:", x)


# Median - The mid point value
# If there are two numbers in the middle, divide the sum of those numbers by two.
# 77, 78, 85, 86, 86, 86, 87, 87, 94, 98, 99, 103
# (86 + 87) / 2 = 86.5
speed2 = [99,86,87,88,86,103,87,94,78,77,85,86]

x2 = numpy.median(speed2)

print("Median:", x2)

# Mode - The most common value
# The Mode value is the value that appears the most number of times:
# 99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86 = 86
speed3 = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x3 = stats.mode(speed)

print("Mode:", x3)

# Standard deviation is a number that describes how spread out the values are.
# A low standard deviation means that most of the numbers are close to the mean (average) value.
# A high standard deviation means that the values are spread out over a wider range.
# the NumPy std() method to find the standard deviation
speed4 = [86,87,88,86,87,85,86]

x4 = numpy.std(speed)

print("std low", x4)


speed5 = [32,111,138,28,59,77,97]

x5 = numpy.std(speed5)

print("std high", x5)


# Percentiles are used in statistics to give you a number that describes the value that a given percent of the values are lower than.
# NumPy percentile() method to find the percentiles
# What is the 75. percentile? The answer is 43, meaning that 75% of the people are 43 or younger.

ages1 = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

y = numpy.percentile(ages1, 75)

print("percentile", y)


# Create an array containing 250 random floats between 0 and 5:
# To create big data sets for testing, we use the Python module NumPy, which comes with a number of methods to create random data sets, of any size.
y1 = numpy.random.uniform(0.0, 5.0, 250)

print("big data set", y1)


# To visualize the data set we can draw a histogram with the data we collected.
# We will use the Python module Matplotlib to draw a histogram.
y2 = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(y2, 5)
plt.show()































