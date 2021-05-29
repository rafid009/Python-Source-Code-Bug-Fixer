import numpy as np 

def function(x):

	n8 = 8
	d3 = 1
	paths = []
	try:
		if x <= 6:
			d3 = 5/d3
			paths.append(1)
		else:
			x = 1/d3
			n8 = n8/d3
			d3 = 2-d3
			paths.append(2)
		if x > 0:
			x = 2*x
			n8 = 9*n8
			paths.append(3)
		else:
			d3 = 5+d3
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