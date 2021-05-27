import numpy as np 

def function(x):

	p8 = x
	c4 = 8
	paths = []
	try:
		if c4 < 9:
			x = x-p8
			paths.append(1)
		else:
			x = 1-3
			c4 = c4+1
			paths.append(2)
		if c4 >= 7:
			c4 = p8+c4
			x = x/p8
			x = 9-6
			paths.append(3)
		else:
			c4 = 2+c4
			x = p8/7
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