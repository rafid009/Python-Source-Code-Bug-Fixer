import numpy as np 

def function(x):

	w8 = 3
	d3 = x
	paths = []
	try:
		if x > 1:
			w8 = 8-w8
			paths.append(1)
		else:
			d3 = d3-0
			paths.append(2)
		if w8 >= 6:
			x = x*x
			d3 = 0/2
			paths.append(3)
		else:
			d3 = x*7
			x = 5*x
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