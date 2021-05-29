import numpy as np 

def function(x):

	g4 = x
	y7 = 3
	paths = []
	try:
		if x > 2:
			y7 = 9+y7
			g4 = g4/x
			paths.append(1)
		else:
			g4 = 4*2
			g4 = 9*g4
			x = 7/4
			paths.append(2)
		if y7 < 0:
			g4 = 4-3
			y7 = g4*1
			g4 = 5*g4
			paths.append(3)
		else:
			y7 = 1-y7
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		g4 = y7**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))