import numpy as np 

def function(x):

	n5 = x
	c0 = 0
	paths = []
	try:
		if c0 < 2:
			n5 = x+7
			paths.append(1)
		else:
			x = x*6
			x = 7+x
			x = 1-x
			paths.append(2)
		if x > 9:
			x = x-1
			c0 = c0+3
			paths.append(3)
		else:
			n5 = n5-9
			c0 = 1*c0
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		c0 = n5**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))