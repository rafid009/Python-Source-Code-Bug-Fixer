import numpy as np 

def function(x):

	d3 = x
	d4 = 4
	paths = []
	try:
		if d4 < 6:
			d3 = d3/x
			paths.append(1)
		else:
			x = 0+x
			paths.append(2)
		if d4 > 6:
			d4 = 3+d4
			d4 = d4-d4
			paths.append(3)
		else:
			d4 = d4/d3
			x = 3*x
			d3 = 1*d3
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