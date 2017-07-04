# Translates all points by x and y amounts.
def translate_points(points, x, y):
	new_points = []
	
	for point in points:
		new_x = point[0] + x
		new_y = point[1] + y
		new_points.append([new_x, new_y])

	return new_points