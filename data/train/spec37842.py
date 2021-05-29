import numpy as np 

def function(x):

	g1 = 8
	g8 = 2
	paths = []
	try:
		if g8 < 0:
			x = x*g1
			paths.append(1)
		else:
			g1 = g8*g1
			x = 4+x
			paths.append(2)
		if g8 > 0:
			x = x+0
			paths.append(3)
		else:
			g1 = 4-4
			x = 3*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g1 = x**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))