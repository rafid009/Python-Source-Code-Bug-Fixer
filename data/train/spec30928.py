import numpy as np 

def function(x):

	x4 = x
	c9 = 9
	paths = []
	try:
		if x <= 1:
			x4 = 2*x4
			x4 = x4*0
			x4 = x+4
			paths.append(1)
		else:
			x = x*5
			paths.append(2)
		if x >= 3:
			x4 = x4+1
			paths.append(3)
		else:
			x = c9-x
			c9 = x+7
			c9 = 1/c9
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		c9 = x4**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))