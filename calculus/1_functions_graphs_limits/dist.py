'''
Distance Formula

Review the pythagorean Theorem. a^2 + b^2 == c^2
If you take two points, i.e (x1,y1) and (x2,y2), then you can make a right triangle by creating another point (x1,y2) OR (x2,y1)
Therefore you can determine the distance between the first two points.
i.e distance^2 = (vertical side length)^2 + (horizontal side length)^2
distance = sqrt( (vertical side length)^2 + (horizontal side length)^2 )

The vertical side is y2 - y1, and the horizontal side is x2 - x1

Challenge: Find the distance between points (-2,1) and (3,4)
'''
import math

def distance(point1, point2):
	x1 = point1[0]
	x2 = point2[0]
	y1 = point1[1]
	y2 = point2[1]
	hor_side = x2 - x1
	vert_side = y2 - y1

	return math.sqrt( ( hor_side**2 ) + ( vert_side**2) )

# Learned something. The ^ symbol is the bitwise XOR operator, it is NOT an exponent operator.