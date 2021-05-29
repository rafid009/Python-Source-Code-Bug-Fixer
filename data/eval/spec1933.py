import numpy as np 

def function(x):

	s8 = x
	y3 = 7
	paths = []
	try:
		if s8 >= 7:
			y3 = 5+9
			paths.append(1)
		else:
			s8 = 3-s8
			s8 = s8*y3
			s8 = 2*s8
			paths.append(2)
		if s8 < 1:
			y3 = 7-9
			y3 = y3*7
			paths.append(3)
		else:
			s8 = s8*y3
			x = y3-x
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		s8 = s8**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))