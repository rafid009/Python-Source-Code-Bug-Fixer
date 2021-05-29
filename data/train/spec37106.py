import numpy as np 

def function(x):

	c8 = x
	g5 = x
	x = 4
	paths = []
	try:
		if g5 <= 4:
			x = g5*3
			paths.append(1)
		else:
			x = 7*9
			x = 9*x
			paths.append(2)
		if c8 <= 0:
			c8 = c8+1
			c8 = c8*8
			g5 = 6-g5
			paths.append(3)
		else:
			g5 = c8/g5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g5 = x**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))