import numpy as np 

def function(x):

	l8 = x
	y0 = 6
	paths = []
	try:
		if l8 > 2:
			l8 = 0/3
			paths.append(1)
		else:
			y0 = 9/7
			l8 = l8*l8
			paths.append(2)
		if y0 <= 7:
			y0 = x-y0
			y0 = 6*l8
			paths.append(3)
		else:
			l8 = y0+l8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y0 = x**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))