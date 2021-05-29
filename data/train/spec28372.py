import numpy as np 

def function(x):

	d3 = 1
	z5 = 2
	paths = []
	try:
		if x > 6:
			d3 = d3/d3
			z5 = x-z5
			d3 = 5+d3
			paths.append(1)
		else:
			x = x*3
			x = 9+3
			z5 = 9/6
			paths.append(2)
		if x < 7:
			d3 = x/d3
			x = x/8
			x = x-2
			paths.append(3)
		else:
			d3 = 5*d3
			d3 = d3*d3
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