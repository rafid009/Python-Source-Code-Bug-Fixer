import numpy as np 

def function(x):

	z0 = x
	d5 = x
	x = 2
	paths = []
	try:
		if z0 < 0:
			d5 = d5-5
			paths.append(1)
		else:
			d5 = d5-z0
			z0 = z0-z0
			z0 = 8+8
			paths.append(2)
		if d5 >= 2:
			z0 = x+8
			d5 = d5-6
			x = 9-x
			paths.append(3)
		else:
			x = x*3
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		d5 = d5**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))