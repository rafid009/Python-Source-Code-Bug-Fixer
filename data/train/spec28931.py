import numpy as np 

def function(x):

	g4 = 1
	k2 = x
	paths = []
	try:
		if x > 2:
			g4 = g4-g4
			k2 = x+3
			paths.append(1)
		else:
			g4 = g4-k2
			paths.append(2)
		if x >= 9:
			k2 = g4-g4
			paths.append(3)
		else:
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g4 = x**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))