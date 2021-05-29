import numpy as np 

def function(x):

	c4 = 5
	u8 = 4
	paths = []
	try:
		if c4 >= 4:
			x = x-6
			paths.append(1)
		else:
			c4 = 0-2
			paths.append(2)
		if x > 2:
			x = x-2
			u8 = u8+6
			paths.append(3)
		else:
			u8 = x+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c4 = x**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))