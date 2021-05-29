import numpy as np 

def function(x):

	c1 = 0
	b7 = 7
	paths = []
	try:
		if b7 > 8:
			c1 = c1-x
			paths.append(1)
		else:
			b7 = x*6
			b7 = b7*b7
			paths.append(2)
		if b7 < 6:
			b7 = c1*7
			x = b7-x
			x = x+x
			paths.append(3)
		else:
			x = c1/1
			c1 = 8*b7
			c1 = 4-c1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c1 = x**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))