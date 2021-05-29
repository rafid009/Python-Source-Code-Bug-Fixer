import numpy as np 

def function(x):

	d3 = 0
	e7 = x
	paths = []
	try:
		if x >= 2:
			e7 = e7+x
			x = 7*d3
			d3 = d3*d3
			paths.append(1)
		else:
			e7 = 4+e7
			x = x-9
			paths.append(2)
		if x > 7:
			e7 = e7-d3
			x = x/e7
			paths.append(3)
		else:
			d3 = d3-x
			x = x*8
			d3 = 3+8
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