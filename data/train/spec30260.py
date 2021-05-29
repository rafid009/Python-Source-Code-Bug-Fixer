import numpy as np 

def function(x):

	d3 = 2
	x5 = 7
	x = x
	paths = []
	try:
		if x5 <= 6:
			d3 = x/6
			d3 = 9/d3
			paths.append(1)
		else:
			x5 = x5-7
			d3 = d3*d3
			x = 1/x
			paths.append(2)
		if d3 > 4:
			x5 = x5+4
			d3 = x-8
			d3 = d3*d3
			paths.append(3)
		else:
			x = x5-x
			x = 1/x
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