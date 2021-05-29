import numpy as np 

def function(x):

	c2 = 1
	b4 = x
	x = 0
	paths = []
	try:
		if x >= 5:
			c2 = c2/7
			c2 = 8/x
			paths.append(1)
		else:
			c2 = c2-x
			x = 1-c2
			paths.append(2)
		if c2 <= 3:
			x = x+4
			paths.append(3)
		else:
			b4 = b4-b4
			b4 = b4/6
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		c2 = b4**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))