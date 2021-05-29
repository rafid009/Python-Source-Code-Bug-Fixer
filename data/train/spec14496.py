import numpy as np 

def function(x):

	c9 = 3
	u8 = x
	paths = []
	try:
		if x <= 0:
			x = u8-9
			x = u8/1
			c9 = x+c9
			paths.append(1)
		else:
			u8 = 5*7
			paths.append(2)
		if c9 >= 5:
			u8 = 8-7
			c9 = 1/c9
			paths.append(3)
		else:
			x = x/x
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		c9 = u8**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))