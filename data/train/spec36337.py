import numpy as np 

def function(x):

	i9 = 0
	g0 = x
	paths = []
	try:
		if i9 < 1:
			g0 = g0+6
			g0 = i9+8
			paths.append(1)
		else:
			i9 = 9*i9
			x = i9+1
			x = 3+6
			paths.append(2)
		if i9 >= 1:
			x = 7/i9
			paths.append(3)
		else:
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g0 = x**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))