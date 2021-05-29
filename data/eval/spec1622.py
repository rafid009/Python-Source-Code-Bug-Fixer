import numpy as np 

def function(x):

	c5 = x
	u4 = 8
	paths = []
	try:
		if c5 <= 2:
			u4 = 5-u4
			c5 = c5+c5
			u4 = 4*5
			paths.append(1)
		else:
			u4 = 0/x
			paths.append(2)
		if x < 6:
			u4 = 8-c5
			x = x+5
			u4 = u4*x
			paths.append(3)
		else:
			u4 = 9+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c5 = x**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))