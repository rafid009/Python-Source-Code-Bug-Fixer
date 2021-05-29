import numpy as np 

def function(x):

	h3 = 8
	d3 = 9
	paths = []
	try:
		if h3 >= 3:
			d3 = 9-d3
			x = x*2
			h3 = d3/6
			paths.append(1)
		else:
			d3 = 1/9
			paths.append(2)
		if x <= 3:
			h3 = h3-8
			x = d3-8
			paths.append(3)
		else:
			d3 = d3/3
			d3 = d3-6
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