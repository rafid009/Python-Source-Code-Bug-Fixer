import numpy as np 

def function(x):

	g0 = x
	l8 = x
	paths = []
	try:
		if g0 < 0:
			g0 = l8-2
			paths.append(1)
		else:
			g0 = 4/x
			g0 = g0-g0
			l8 = 9+2
			paths.append(2)
		if g0 < 5:
			l8 = l8*6
			g0 = g0+3
			paths.append(3)
		else:
			l8 = l8*6
			g0 = 0-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l8 = x**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))