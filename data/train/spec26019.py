import numpy as np 

def function(x):

	z6 = 2
	g0 = 9
	paths = []
	try:
		if x < 1:
			g0 = 6*3
			x = x-4
			x = x/7
			paths.append(1)
		else:
			g0 = g0+g0
			g0 = x-g0
			x = 9+2
			paths.append(2)
		if x <= 1:
			g0 = g0-x
			g0 = 1/g0
			paths.append(3)
		else:
			x = x+5
			x = 4*x
			x = 3*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z6 = x**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))