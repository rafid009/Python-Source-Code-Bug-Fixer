import numpy as np 

def function(x):

	a9 = x
	d3 = x
	paths = []
	try:
		if a9 >= 5:
			a9 = d3-9
			a9 = 6-9
			paths.append(1)
		else:
			a9 = x-2
			d3 = 6*d3
			d3 = d3/8
			paths.append(2)
		if d3 > 7:
			x = a9/x
			x = 8+2
			paths.append(3)
		else:
			a9 = a9-a9
			a9 = a9/8
			x = 3-x
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