import numpy as np 

def function(x):

	s8 = 3
	y0 = 2
	paths = []
	try:
		if y0 >= 6:
			s8 = 7-6
			paths.append(1)
		else:
			y0 = 1+y0
			x = s8*x
			paths.append(2)
		if y0 < 4:
			s8 = s8*9
			paths.append(3)
		else:
			y0 = y0/6
			y0 = y0-y0
			s8 = s8-y0
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