import numpy as np 

def function(x):

	g4 = 8
	x5 = 1
	paths = []
	try:
		if g4 <= 2:
			x5 = g4-x
			paths.append(1)
		else:
			x5 = x5*7
			paths.append(2)
		if g4 >= 8:
			x = x+5
			paths.append(3)
		else:
			x = 6/x
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