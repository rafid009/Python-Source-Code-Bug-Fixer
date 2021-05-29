import numpy as np 

def function(x):

	y1 = x
	z8 = 8
	paths = []
	try:
		if z8 > 8:
			z8 = 4/9
			z8 = z8/6
			paths.append(1)
		else:
			y1 = 6-y1
			paths.append(2)
		if y1 < 8:
			y1 = 5+9
			y1 = z8/y1
			y1 = z8+6
			paths.append(3)
		else:
			x = x/9
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