import numpy as np 

def function(x):

	c3 = 6
	g9 = x
	paths = []
	try:
		if g9 >= 1:
			c3 = c3+8
			x = 7/x
			x = x+5
			paths.append(1)
		else:
			g9 = 5-g9
			c3 = c3/9
			g9 = 9+c3
			paths.append(2)
		if g9 >= 9:
			g9 = g9*g9
			c3 = 8/c3
			paths.append(3)
		else:
			c3 = g9*g9
			c3 = 5/5
			g9 = 4*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g9 = x**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))