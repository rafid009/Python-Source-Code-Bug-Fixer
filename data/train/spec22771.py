import numpy as np 

def function(x):

	g6 = 1
	g8 = x
	paths = []
	try:
		if g8 < 3:
			g8 = g8+x
			paths.append(1)
		else:
			x = x+9
			g8 = g8/5
			paths.append(2)
		if g8 >= 5:
			g8 = 8-g8
			g6 = x*g8
			g8 = g8-g6
			paths.append(3)
		else:
			x = 5/6
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		g8 = g6**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))