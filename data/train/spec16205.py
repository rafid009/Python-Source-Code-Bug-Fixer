import numpy as np 

def function(x):

	k2 = x
	g3 = 3
	paths = []
	try:
		if x >= 5:
			x = g3+x
			k2 = x/k2
			g3 = 0-8
			paths.append(1)
		else:
			g3 = 1-x
			x = x*6
			k2 = 3-k2
			paths.append(2)
		if g3 < 1:
			g3 = g3-2
			g3 = g3/8
			paths.append(3)
		else:
			g3 = 1-g3
			g3 = x*g3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g3 = x**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))