import numpy as np 

def function(x):

	y6 = 3
	d3 = 1
	paths = []
	try:
		if d3 <= 6:
			x = x-3
			paths.append(1)
		else:
			y6 = 1/y6
			x = 4/x
			paths.append(2)
		if d3 >= 8:
			x = 4*y6
			paths.append(3)
		else:
			d3 = 3/d3
			y6 = y6/7
			d3 = d3-6
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