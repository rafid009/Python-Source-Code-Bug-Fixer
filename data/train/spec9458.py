import numpy as np 

def function(x):

	u7 = x
	c4 = 6
	paths = []
	try:
		if u7 > 5:
			x = x+3
			paths.append(1)
		else:
			c4 = c4-x
			x = x/8
			paths.append(2)
		if c4 > 9:
			c4 = c4*8
			x = x*4
			x = c4+5
			paths.append(3)
		else:
			x = x-0
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		c4 = u7**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))