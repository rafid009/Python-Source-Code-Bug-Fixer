import numpy as np 

def function(x):

	h4 = x
	g7 = 3
	paths = []
	try:
		if x < 4:
			x = x-h4
			paths.append(1)
		else:
			x = x+4
			x = 2-x
			x = x+6
			paths.append(2)
		if g7 > 1:
			g7 = g7-3
			paths.append(3)
		else:
			g7 = h4/g7
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