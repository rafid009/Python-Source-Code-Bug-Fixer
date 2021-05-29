import numpy as np 

def function(x):

	d3 = x
	z1 = x
	x = 2
	paths = []
	try:
		if x > 6:
			d3 = 7+d3
			z1 = z1-5
			x = z1/d3
			paths.append(1)
		else:
			x = 3+x
			paths.append(2)
		if d3 <= 6:
			z1 = z1-8
			paths.append(3)
		else:
			x = x-9
			d3 = 7/x
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d3 = x**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))