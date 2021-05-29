import numpy as np 

def function(x):

	g9 = x
	g7 = x
	x = 6
	paths = []
	try:
		if g9 <= 6:
			x = 6-x
			g7 = 5+g7
			x = x-5
			paths.append(1)
		else:
			g7 = 9+g7
			x = g9-g7
			g9 = g9+x
			paths.append(2)
		if x <= 0:
			g9 = g9+7
			g7 = g7-2
			paths.append(3)
		else:
			g9 = g9/g9
			x = x+4
			g7 = g7-9
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