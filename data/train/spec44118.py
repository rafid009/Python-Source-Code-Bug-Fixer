import numpy as np 

def function(x):

	z5 = 6
	y3 = 2
	paths = []
	try:
		if z5 >= 4:
			y3 = x/4
			x = 1/x
			z5 = 2+z5
			paths.append(1)
		else:
			x = 3*3
			z5 = 8+z5
			paths.append(2)
		if z5 <= 2:
			y3 = 1*9
			y3 = x-x
			x = x/9
			paths.append(3)
		else:
			z5 = 7/z5
			y3 = 7-y3
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