import numpy as np 

def function(x):

	g0 = 8
	d3 = x
	paths = []
	try:
		if d3 >= 2:
			d3 = d3-d3
			d3 = d3*1
			d3 = d3*7
			paths.append(1)
		else:
			d3 = 8-d3
			d3 = 6*d3
			paths.append(2)
		if d3 <= 7:
			x = 6-g0
			g0 = 5*x
			paths.append(3)
		else:
			x = 1-x
			g0 = 0+g0
			x = 3+x
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