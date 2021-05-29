import numpy as np 

def function(x):

	z7 = x
	d3 = x
	paths = []
	try:
		if d3 < 0:
			x = x/3
			d3 = x/d3
			x = x-x
			paths.append(1)
		else:
			x = x/7
			z7 = d3-x
			paths.append(2)
		if x >= 2:
			x = d3+6
			paths.append(3)
		else:
			d3 = 4/d3
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		z7 = z7**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))