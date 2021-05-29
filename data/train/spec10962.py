import numpy as np 

def function(x):

	x9 = 6
	g7 = x
	paths = []
	try:
		if x > 6:
			x9 = g7/4
			x9 = x9-9
			paths.append(1)
		else:
			x9 = x9+x
			g7 = g7-2
			paths.append(2)
		if x < 8:
			g7 = 2*2
			x9 = g7/3
			g7 = 6/g7
			paths.append(3)
		else:
			g7 = g7*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x9 = x**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))