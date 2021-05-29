import numpy as np 

def function(x):

	g7 = 8
	d3 = 1
	paths = []
	try:
		if g7 <= 7:
			g7 = 3/g7
			d3 = x/4
			paths.append(1)
		else:
			x = x/2
			g7 = d3-5
			g7 = 6+g7
			paths.append(2)
		if g7 < 2:
			x = g7+x
			d3 = 6+5
			g7 = g7/3
			paths.append(3)
		else:
			g7 = x+g7
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