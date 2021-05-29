import numpy as np 

def function(x):

	c2 = x
	u8 = 3
	paths = []
	try:
		if x < 3:
			u8 = u8-x
			c2 = c2-9
			paths.append(1)
		else:
			x = 6/x
			paths.append(2)
		if x < 2:
			x = x*1
			c2 = c2-u8
			paths.append(3)
		else:
			u8 = u8-7
			u8 = u8-1
			x = 2*7
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