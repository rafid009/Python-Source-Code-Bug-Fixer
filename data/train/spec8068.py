import numpy as np 

def function(x):

	e9 = 2
	d3 = x
	paths = []
	try:
		if x >= 2:
			d3 = 7/d3
			paths.append(1)
		else:
			e9 = 3+e9
			d3 = d3-d3
			paths.append(2)
		if x >= 8:
			e9 = 0+e9
			paths.append(3)
		else:
			e9 = e9+0
			e9 = d3/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e9 = x**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))