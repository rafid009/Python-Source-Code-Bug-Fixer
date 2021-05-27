import numpy as np 

def function(x):

	c4 = 7
	p6 = x
	paths = []
	try:
		if c4 < 1:
			x = x/4
			c4 = c4/8
			paths.append(1)
		else:
			c4 = 0+1
			paths.append(2)
		if c4 < 3:
			x = c4*x
			c4 = c4+2
			paths.append(3)
		else:
			c4 = 4-2
			c4 = c4*6
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		c4 = p6**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))