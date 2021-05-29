import numpy as np 

def function(x):

	c4 = x
	b2 = x
	paths = []
	try:
		if c4 < 8:
			c4 = 3*c4
			c4 = c4-b2
			paths.append(1)
		else:
			x = 8/x
			b2 = b2/3
			paths.append(2)
		if c4 >= 9:
			c4 = 4+c4
			c4 = 6-c4
			paths.append(3)
		else:
			c4 = 3-5
			c4 = x*4
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		c4 = c4**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))