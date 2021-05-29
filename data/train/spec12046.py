import numpy as np 

def function(x):

	g7 = x
	c6 = x
	paths = []
	try:
		if g7 > 6:
			g7 = 1*g7
			g7 = g7*8
			paths.append(1)
		else:
			g7 = x+4
			g7 = g7+x
			paths.append(2)
		if c6 <= 1:
			g7 = g7-2
			paths.append(3)
		else:
			x = x*c6
			g7 = 6-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c6 = x**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))