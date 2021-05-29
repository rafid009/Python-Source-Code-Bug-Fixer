import numpy as np 

def function(x):

	g7 = 3
	v1 = 6
	x = 4
	paths = []
	try:
		if x >= 9:
			g7 = g7*9
			paths.append(1)
		else:
			g7 = 1*8
			x = 3*x
			x = v1-x
			paths.append(2)
		if v1 > 7:
			g7 = 9*4
			g7 = 0/g7
			paths.append(3)
		else:
			g7 = 4*x
			g7 = 0-g7
			v1 = v1+6
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