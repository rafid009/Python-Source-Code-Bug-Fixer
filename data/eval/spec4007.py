import numpy as np 

def function(x):

	c3 = x
	u7 = x
	paths = []
	try:
		if u7 > 2:
			u7 = 9*8
			c3 = 9/8
			paths.append(1)
		else:
			u7 = 4/x
			paths.append(2)
		if u7 <= 6:
			c3 = c3-u7
			c3 = c3*4
			paths.append(3)
		else:
			x = 2+x
			u7 = x/u7
			x = x-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c3 = x**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))