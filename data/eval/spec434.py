import numpy as np 

def function(x):

	r9 = 7
	d3 = 8
	paths = []
	try:
		if r9 < 5:
			d3 = 1+6
			paths.append(1)
		else:
			x = x*6
			d3 = d3/7
			d3 = d3*r9
			paths.append(2)
		if r9 >= 8:
			d3 = d3*r9
			r9 = r9/d3
			paths.append(3)
		else:
			d3 = 0/d3
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