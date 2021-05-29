import numpy as np 

def function(x):

	y2 = 7
	x0 = 7
	paths = []
	try:
		if x0 <= 3:
			y2 = 5/3
			x = 1-5
			x0 = 2/5
			paths.append(1)
		else:
			x0 = x0-4
			y2 = y2/6
			paths.append(2)
		if y2 <= 0:
			x0 = 6-x
			x = y2*x
			y2 = 4/y2
			paths.append(3)
		else:
			x = 6*x
			y2 = x/3
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