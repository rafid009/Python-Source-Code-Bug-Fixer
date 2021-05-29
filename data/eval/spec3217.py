import numpy as np 

def function(x):

	d3 = x
	h7 = 3
	paths = []
	try:
		if x < 8:
			h7 = 9*h7
			d3 = 3+d3
			h7 = h7/5
			paths.append(1)
		else:
			x = x-4
			x = d3*d3
			h7 = 8+2
			paths.append(2)
		if h7 > 6:
			x = 2-x
			h7 = 2*h7
			d3 = h7+1
			paths.append(3)
		else:
			d3 = d3+2
			h7 = h7-0
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