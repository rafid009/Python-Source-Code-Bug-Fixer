import numpy as np 

def function(x):

	d3 = x
	g5 = x
	paths = []
	try:
		if g5 > 5:
			d3 = 6/g5
			x = 6-x
			paths.append(1)
		else:
			x = g5+4
			paths.append(2)
		if d3 < 6:
			g5 = g5+d3
			g5 = 6-3
			paths.append(3)
		else:
			d3 = d3/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g5 = x**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))