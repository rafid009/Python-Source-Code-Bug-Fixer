import numpy as np 

def function(x):

	c2 = 1
	g1 = 4
	paths = []
	try:
		if g1 <= 7:
			g1 = c2-8
			g1 = g1+6
			paths.append(1)
		else:
			c2 = x*3
			c2 = 9-7
			x = x*1
			paths.append(2)
		if x > 0:
			x = x-3
			g1 = 5*g1
			x = x+0
			paths.append(3)
		else:
			c2 = 9/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c2 = x**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))