import numpy as np 

def function(x):

	c1 = 9
	u4 = x
	paths = []
	try:
		if u4 >= 6:
			u4 = x/7
			paths.append(1)
		else:
			u4 = u4+u4
			paths.append(2)
		if c1 < 0:
			c1 = 9/c1
			x = x-8
			c1 = 3+c1
			paths.append(3)
		else:
			c1 = c1+7
			x = 6/x
			x = 6+x
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		c1 = u4**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))