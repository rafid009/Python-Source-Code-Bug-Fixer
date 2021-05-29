import numpy as np 

def function(x):

	z8 = x
	d4 = x
	paths = []
	try:
		if x < 3:
			d4 = d4/x
			d4 = 6+d4
			z8 = z8-0
			paths.append(1)
		else:
			z8 = 0-d4
			d4 = d4/6
			x = z8/x
			paths.append(2)
		if x > 3:
			z8 = z8/6
			x = 3-6
			d4 = d4/6
			paths.append(3)
		else:
			d4 = 3-0
			d4 = 8/9
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