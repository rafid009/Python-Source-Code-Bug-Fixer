import numpy as np 

def function(x):

	g6 = 9
	i6 = 7
	paths = []
	try:
		if g6 >= 6:
			g6 = 7+2
			g6 = 7*g6
			g6 = g6-7
			paths.append(1)
		else:
			g6 = x-4
			x = 7-x
			x = x/3
			paths.append(2)
		if i6 > 6:
			i6 = i6*x
			g6 = 9-x
			paths.append(3)
		else:
			g6 = 4/g6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g6 = x**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))