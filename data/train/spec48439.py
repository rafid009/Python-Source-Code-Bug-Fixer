import numpy as np 

def function(x):

	d3 = 1
	g9 = 9
	paths = []
	try:
		if d3 > 0:
			g9 = g9-g9
			d3 = 6-d3
			d3 = d3*1
			paths.append(1)
		else:
			x = 3+6
			g9 = g9+4
			d3 = g9*x
			paths.append(2)
		if g9 <= 1:
			g9 = g9*4
			paths.append(3)
		else:
			g9 = g9/1
			g9 = 2*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d3 = x**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))