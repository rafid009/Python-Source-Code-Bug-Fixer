import numpy as np 

def function(x):

	d9 = 3
	g7 = x
	paths = []
	try:
		if d9 < 5:
			d9 = d9-3
			g7 = g7/3
			g7 = 6-g7
			paths.append(1)
		else:
			d9 = d9/x
			paths.append(2)
		if x >= 8:
			d9 = d9-g7
			g7 = g7*g7
			x = g7-9
			paths.append(3)
		else:
			g7 = 9+g7
			x = x+3
			d9 = d9+9
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