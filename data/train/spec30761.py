import numpy as np 

def function(x):

	c9 = 1
	u8 = 4
	paths = []
	try:
		if x >= 0:
			x = 0-x
			u8 = c9-7
			c9 = 8+x
			paths.append(1)
		else:
			x = 4+x
			c9 = 1/c9
			paths.append(2)
		if c9 >= 6:
			u8 = 9-u8
			c9 = c9*8
			x = 3+x
			paths.append(3)
		else:
			c9 = 4-c9
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		u8 = c9**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))