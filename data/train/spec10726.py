import numpy as np 

def function(x):

	g7 = x
	b1 = 3
	paths = []
	try:
		if g7 >= 5:
			x = 8/x
			paths.append(1)
		else:
			g7 = g7/8
			b1 = g7*g7
			x = 9+b1
			paths.append(2)
		if g7 <= 3:
			b1 = b1-g7
			g7 = g7*g7
			g7 = 6*g7
			paths.append(3)
		else:
			g7 = 4+g7
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		g7 = b1**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))