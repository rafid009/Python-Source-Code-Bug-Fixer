import numpy as np 

def function(x):

	g7 = 7
	s0 = x
	paths = []
	try:
		if g7 >= 6:
			g7 = g7*5
			s0 = 6-s0
			g7 = g7+7
			paths.append(1)
		else:
			g7 = g7+7
			paths.append(2)
		if g7 < 7:
			g7 = g7+g7
			paths.append(3)
		else:
			g7 = x+2
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