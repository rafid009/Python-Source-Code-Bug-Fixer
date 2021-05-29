import numpy as np 

def function(x):

	g7 = 6
	y3 = x
	paths = []
	try:
		if g7 > 0:
			g7 = g7+6
			paths.append(1)
		else:
			g7 = 6+5
			g7 = 2*g7
			paths.append(2)
		if y3 <= 6:
			x = g7/y3
			paths.append(3)
		else:
			x = x+x
			x = x-g7
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		g7 = y3**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))