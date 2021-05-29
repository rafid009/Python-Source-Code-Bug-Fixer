import numpy as np 

def function(x):

	u8 = x
	c9 = x
	paths = []
	try:
		if c9 <= 5:
			c9 = c9*4
			paths.append(1)
		else:
			c9 = 8+c9
			c9 = x-c9
			paths.append(2)
		if u8 >= 1:
			x = 9-3
			x = x-0
			c9 = c9*1
			paths.append(3)
		else:
			x = x+0
			x = x+x
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		c9 = c9**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))