import numpy as np 

def function(x):

	l7 = 8
	c0 = 6
	paths = []
	try:
		if x >= 3:
			x = x*4
			x = 2+c0
			paths.append(1)
		else:
			c0 = c0/7
			l7 = 1+l7
			x = c0/x
			paths.append(2)
		if c0 >= 7:
			x = 9/x
			c0 = c0/2
			x = 0-x
			paths.append(3)
		else:
			c0 = c0-7
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		c0 = c0**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))