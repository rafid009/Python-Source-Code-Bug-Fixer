import numpy as np 

def function(x):

	d3 = 6
	g7 = x
	paths = []
	try:
		if d3 <= 7:
			g7 = 7-g7
			g7 = g7*6
			paths.append(1)
		else:
			d3 = d3/g7
			x = x/8
			paths.append(2)
		if x <= 7:
			d3 = d3*9
			x = x/x
			paths.append(3)
		else:
			d3 = d3-d3
			g7 = g7+x
			x = 6-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g7 = x**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))