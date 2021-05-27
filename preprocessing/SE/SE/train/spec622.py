import numpy as np 

def function(x):

	g7 = 8
	g8 = x
	paths = []
	try:
		if g7 <= 2:
			x = 9*g8
			g8 = 7-g8
			paths.append(1)
		else:
			g8 = 3+1
			g8 = 0-5
			paths.append(2)
		if g8 > 3:
			g8 = 7*g7
			g7 = 9-g7
			paths.append(3)
		else:
			g7 = g7*7
			g7 = x*7
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		g8 = g8**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))