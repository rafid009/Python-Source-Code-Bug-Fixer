import numpy as np 

def function(x):

	y0 = 2
	s0 = 3
	paths = []
	try:
		if s0 >= 5:
			y0 = y0-3
			paths.append(1)
		else:
			y0 = y0+y0
			y0 = y0+5
			x = x/7
			paths.append(2)
		if s0 > 6:
			y0 = 7/y0
			x = 9+s0
			paths.append(3)
		else:
			y0 = 8/s0
			y0 = y0-3
			s0 = y0-s0
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		x = y0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))