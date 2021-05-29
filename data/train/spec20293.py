import numpy as np 

def function(x):

	g6 = x
	a0 = x
	paths = []
	try:
		if a0 <= 3:
			g6 = 1-g6
			paths.append(1)
		else:
			g6 = 0-x
			paths.append(2)
		if x < 8:
			x = x+6
			g6 = g6-x
			paths.append(3)
		else:
			a0 = x+4
			g6 = a0+x
			g6 = a0/7
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		g6 = a0**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))