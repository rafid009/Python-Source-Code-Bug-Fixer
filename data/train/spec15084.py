import numpy as np 

def function(x):

	g8 = 3
	c3 = x
	paths = []
	try:
		if c3 >= 5:
			c3 = c3-7
			x = x-g8
			c3 = c3*c3
			paths.append(1)
		else:
			g8 = g8-c3
			g8 = 7*g8
			x = 1/c3
			paths.append(2)
		if c3 > 4:
			c3 = 7-c3
			g8 = 3/8
			x = 3-4
			paths.append(3)
		else:
			g8 = 9+4
			c3 = 4+2
			x = x*0
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