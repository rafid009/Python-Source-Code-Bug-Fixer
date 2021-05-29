import numpy as np 

def function(x):

	c2 = x
	g8 = 2
	paths = []
	try:
		if g8 < 6:
			x = 6*x
			c2 = c2+g8
			paths.append(1)
		else:
			x = x*3
			x = c2-x
			paths.append(2)
		if g8 >= 5:
			x = 0-3
			paths.append(3)
		else:
			g8 = x/1
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