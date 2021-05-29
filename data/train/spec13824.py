import numpy as np 

def function(x):

	u8 = x
	c6 = x
	paths = []
	try:
		if x > 6:
			c6 = c6-x
			paths.append(1)
		else:
			x = 9*x
			c6 = 4/c6
			x = 8*4
			paths.append(2)
		if c6 <= 5:
			u8 = 7+5
			c6 = c6-9
			c6 = c6+1
			paths.append(3)
		else:
			x = u8-1
			u8 = 5+u8
			u8 = u8/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c6 = x**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))