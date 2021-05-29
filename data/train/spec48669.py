import numpy as np 

def function(x):

	g8 = 1
	c1 = x
	paths = []
	try:
		if g8 >= 3:
			c1 = 6*5
			g8 = g8*x
			g8 = g8-2
			paths.append(1)
		else:
			c1 = 5*2
			c1 = g8*5
			g8 = g8/g8
			paths.append(2)
		if c1 >= 1:
			x = x-8
			paths.append(3)
		else:
			g8 = g8*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g8 = x**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))