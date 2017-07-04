from dist import distance
from is_right import is_right_triangle
from midpoint import midpoint
from translating_points_plane import translate_points

def test_distance_formula():
	point1 = [-2,1]
	point2 = [3,4]
	dist = distance(point1, point2)
	assert round(dist, 2) == 5.83

def test_distance_formula2():
	point1 = [-2,1]
	point2 = [2,4]
	dist = distance(point1, point2)
	assert round(dist, 2) == 5

def test_is_right_triangle():
	point1 = [2,1]
	point2 = [4,0]
	point3 = [5,7]
	is_right = is_right_triangle(point1, point2, point3)
	assert is_right == True

def test_is_right_triangle2():
	point1 = [2,-1]
	point2 = [5,5]
	point3 = [6,-3]
	is_right = is_right_triangle(point1, point2, point3)
	assert is_right == True

def test_distance_formula3():
	point1 = [20,5]
	point2 = [50,45]
	dist = distance(point1, point2)
	return dist == 50

def test_midpoint_formula():
	point1 = [-5,-3]
	point2 = [9,3]
	mid = midpoint(point1,point2)
	assert mid == [2,0]

def test_midpoint_formula2():
	point1 = [-6,2]
	point2 = [2,8]
	mid = midpoint(point1,point2)
	assert mid == [-2,5]

def test_midpoint_formula2():
	point1 = [1998,9.0]
	point2 = [2000,11.6]
	mid = midpoint(point1,point2)
	assert mid == [1999,10.3]

def test_midpoint_formula3():
	point1 = [1998,161.3]
	point2 = [2000,184.6]
	mid = midpoint(point1,point2)
	assert mid == [1999,172.95]

def test_translate_points():
	points = [[1,0],[3,2],[3,6],[1,4]]
	new_points = translate_points( points, 4, -2)
	assert new_points == [[5,-2],[7,0],[7,4],[5,2]]