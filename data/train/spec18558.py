import numpy as np 

def function(x):

	g8 = x
	q7 = x
	paths = []
	try:
		if g8 > 6:
			g8 = g8+2
			paths.append(1)
		else:
			q7 = q7+7
			paths.append(2)
		if g8 >= 1:
			g8 = x-g8
			paths.append(3)
		else:
			x = x/2
			g8 = g8+3
			g8 = 9-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g8 = x**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))