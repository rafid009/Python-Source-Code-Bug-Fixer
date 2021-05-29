import numpy as np 

def function(x):

	z0 = x
	d8 = 6
	paths = []
	try:
		if d8 <= 0:
			z0 = 5-7
			paths.append(1)
		else:
			d8 = 8/d8
			d8 = d8/1
			paths.append(2)
		if z0 < 9:
			z0 = z0-8
			d8 = d8*3
			z0 = 5/9
			paths.append(3)
		else:
			x = x+7
			x = 3/x
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