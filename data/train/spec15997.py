import numpy as np 

def function(x):

	d3 = x
	x3 = 2
	x = x
	paths = []
	try:
		if x >= 5:
			x3 = 9-2
			x3 = x+2
			paths.append(1)
		else:
			x3 = x3*3
			d3 = d3-x3
			d3 = d3*3
			paths.append(2)
		if x3 < 3:
			x3 = x3*x3
			paths.append(3)
		else:
			d3 = 1/4
			x3 = x3-4
			x = d3-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x3 = x**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))