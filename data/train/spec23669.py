import numpy as np 

def function(x):

	l9 = 0
	g7 = 7
	x = x
	paths = []
	try:
		if x >= 3:
			x = g7/x
			paths.append(1)
		else:
			g7 = x*g7
			g7 = 3*g7
			paths.append(2)
		if x >= 5:
			l9 = 4-g7
			g7 = x+l9
			paths.append(3)
		else:
			x = 9+g7
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		g7 = g7**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))