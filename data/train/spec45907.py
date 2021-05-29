import numpy as np 

def function(x):

	d3 = 2
	w0 = 7
	paths = []
	try:
		if d3 >= 1:
			d3 = x*5
			paths.append(1)
		else:
			w0 = w0-w0
			paths.append(2)
		if x < 6:
			x = w0-x
			w0 = w0*d3
			x = x+6
			paths.append(3)
		else:
			d3 = 6/x
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		x = d3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))