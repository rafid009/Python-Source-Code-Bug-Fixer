import numpy as np 

def function(x):

	g5 = x
	g6 = x
	paths = []
	try:
		if g5 >= 5:
			g6 = x+x
			paths.append(1)
		else:
			g5 = 0+g6
			g5 = 7*g5
			g5 = g5*5
			paths.append(2)
		if g5 < 6:
			g5 = 1*g5
			x = g5+2
			paths.append(3)
		else:
			g5 = 1-g5
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		g6 = g6**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))