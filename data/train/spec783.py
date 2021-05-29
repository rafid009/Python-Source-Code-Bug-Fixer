import numpy as np 

def function(x):

	d3 = 9
	h2 = 5
	paths = []
	try:
		if d3 >= 2:
			d3 = 8/d3
			paths.append(1)
		else:
			h2 = h2-6
			h2 = x+x
			d3 = d3/x
			paths.append(2)
		if h2 < 6:
			d3 = 9+d3
			paths.append(3)
		else:
			d3 = d3-8
			d3 = h2/d3
			x = 7-8
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