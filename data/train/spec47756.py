import numpy as np 

def function(x):

	x0 = 1
	y4 = x
	paths = []
	try:
		if x0 >= 3:
			x0 = y4-y4
			paths.append(1)
		else:
			y4 = y4/y4
			paths.append(2)
		if x0 <= 1:
			y4 = x-y4
			paths.append(3)
		else:
			y4 = x0*4
			x0 = y4*x
			x0 = 2-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y4 = x**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))