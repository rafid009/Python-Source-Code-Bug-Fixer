import numpy as np 

def function(x):

	e7 = 3
	d3 = 5
	paths = []
	try:
		if d3 > 0:
			x = 2*x
			d3 = d3-9
			paths.append(1)
		else:
			x = d3-x
			d3 = d3-0
			paths.append(2)
		if d3 < 9:
			e7 = 8-e7
			paths.append(3)
		else:
			x = 7-x
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