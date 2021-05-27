import numpy as np 

def function(x):

	g8 = 2
	t7 = 5
	paths = []
	try:
		if t7 >= 2:
			x = g8*x
			paths.append(1)
		else:
			x = x-x
			x = 7-t7
			g8 = 3/x
			paths.append(2)
		if x <= 2:
			g8 = g8*7
			paths.append(3)
		else:
			x = 6/x
			g8 = g8/g8
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