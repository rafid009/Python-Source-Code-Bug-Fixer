import numpy as np 

def function(x):

	g7 = 2
	n3 = 9
	paths = []
	try:
		if g7 >= 9:
			g7 = x+g7
			paths.append(1)
		else:
			x = x/x
			g7 = g7-7
			paths.append(2)
		if x >= 0:
			n3 = g7-n3
			g7 = g7-x
			n3 = 9+n3
			paths.append(3)
		else:
			x = g7-1
			n3 = n3*4
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