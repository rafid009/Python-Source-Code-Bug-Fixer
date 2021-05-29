import numpy as np 

def function(x):

	y5 = x
	y0 = x
	paths = []
	try:
		if x < 8:
			x = 6*x
			paths.append(1)
		else:
			y0 = y0+3
			paths.append(2)
		if y5 < 5:
			x = 0-x
			paths.append(3)
		else:
			y5 = y5/y5
			y5 = 4-y5
			y0 = 4+0
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