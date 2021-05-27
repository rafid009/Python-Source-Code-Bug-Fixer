import numpy as np 

def function(x):

	s8 = x
	y3 = 8
	paths = []
	try:
		if s8 > 7:
			y3 = 2/y3
			y3 = 6-s8
			paths.append(1)
		else:
			y3 = 9*6
			x = y3/4
			paths.append(2)
		if s8 >= 2:
			y3 = y3+6
			paths.append(3)
		else:
			x = s8-x
			s8 = y3*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))