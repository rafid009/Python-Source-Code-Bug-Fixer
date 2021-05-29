import numpy as np 

def function(x):

	g6 = 7
	f0 = 9
	paths = []
	try:
		if g6 < 3:
			g6 = g6+g6
			paths.append(1)
		else:
			g6 = g6+g6
			paths.append(2)
		if g6 <= 8:
			f0 = 6-x
			f0 = 8-f0
			paths.append(3)
		else:
			g6 = g6/x
			f0 = g6+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))