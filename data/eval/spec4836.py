import numpy as np 

def function(x):

	d3 = x
	d4 = 4
	paths = []
	try:
		if x >= 7:
			d4 = d3/4
			d3 = d3/4
			paths.append(1)
		else:
			d3 = 3*x
			d3 = x*1
			d3 = d3/x
			paths.append(2)
		if d4 > 8:
			x = 0/8
			d3 = 1-d3
			paths.append(3)
		else:
			d4 = x+8
			x = d3-2
			d3 = d3+6
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