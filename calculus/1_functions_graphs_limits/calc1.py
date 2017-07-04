# 1.1 The Cartesian Plane and the distance formula
import numpy as np
import matplotlib.pyplot as plt

''' Here's a cool way to generate 50 random points. But not the challenge in the book.
N = 50
x = np.random.rand(N) * 10
y = np.random.rand(N) * 10
'''
x = []
y = []
def make_points(a,b):
	x.append(a)
	y.append(b)

make_points(-1,2)
make_points(3,4)
make_points(0,0)
make_points(3,0)
make_points(-2,-3)

plt.scatter(x,y)
plt.show()

# Apparently Cartesian plane is named after Rene Descartes.