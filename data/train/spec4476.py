import numpy as np 

def function(x):

	g8 = x
	g6 = 4
	paths = []
	try:
		if g8 <= 1:
			g8 = 7+8
			paths.append(1)
		else:
			g8 = g8+g6
			paths.append(2)
		if g6 > 2:
			g8 = 9*g6
			g6 = 6-4
			paths.append(3)
		else:
			g6 = g8+g6
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