import numpy as np 

def function(x):

	g2 = x
	c7 = x
	paths = []
	try:
		if c7 > 8:
			c7 = 3+2
			x = g2/x
			paths.append(1)
		else:
			x = x+3
			g2 = 3-7
			c7 = c7+g2
			paths.append(2)
		if g2 <= 9:
			x = x-7
			x = c7+7
			g2 = x*x
			paths.append(3)
		else:
			c7 = c7+g2
			x = 3*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g2 = x**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))