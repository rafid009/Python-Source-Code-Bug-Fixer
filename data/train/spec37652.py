import numpy as np 

def function(x):

	y0 = 3
	x0 = 1
	paths = []
	try:
		if x0 < 3:
			x0 = x0+7
			x0 = 9/8
			paths.append(1)
		else:
			x = 5-x
			y0 = 3-y0
			paths.append(2)
		if y0 <= 1:
			x0 = x0+4
			paths.append(3)
		else:
			y0 = y0/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x0 = x**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))