import numpy as np 

def function(x):

	d3 = 9
	o7 = 3
	paths = []
	try:
		if o7 >= 8:
			o7 = o7-1
			d3 = 8*d3
			x = x*x
			paths.append(1)
		else:
			d3 = 8-1
			d3 = 9/4
			paths.append(2)
		if o7 > 8:
			x = x-6
			d3 = d3-8
			paths.append(3)
		else:
			d3 = 2/d3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o7 = x**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))