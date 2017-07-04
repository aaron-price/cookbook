from dist import distance

def is_right_triangle(point1,point2,point3):
	d1 = distance(point1, point2)
	d2 = distance(point2, point3)
	d3 = distance(point3, point1)
	all_points = [d1,d2,d3]
	all_points.sort()
	print(all_points)
	a2_and_b2 = round(all_points[0]**2 + all_points[1]**2, 2)
	c2 = round(all_points[2]**2,2)

	return a2_and_b2 == c2