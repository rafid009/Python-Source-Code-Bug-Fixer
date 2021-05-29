import numpy as np 

def function(x):

	y3 = x
	z5 = x
	paths = []
	try:
		if z5 < 3:
			x = x/x
			x = x-5
			paths.append(1)
		else:
			x = 4/4
			paths.append(2)
		if z5 > 5:
			x = 1/x
			y3 = y3*x
			y3 = 8-y3
			paths.append(3)
		else:
			z5 = z5+2
			y3 = y3/x
			y3 = y3/4
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