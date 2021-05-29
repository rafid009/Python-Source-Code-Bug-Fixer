import numpy as np 

def function(x):

	c0 = 8
	c2 = 6
	paths = []
	try:
		if c2 > 9:
			x = x-3
			paths.append(1)
		else:
			c2 = c0-3
			c0 = 8-x
			paths.append(2)
		if c2 <= 0:
			x = c2*8
			x = x-6
			x = 5*1
			paths.append(3)
		else:
			c2 = c0-c2
			x = 4*x
			x = 2*5
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		c2 = c2**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))