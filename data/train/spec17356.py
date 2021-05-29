import numpy as np 

def function(x):

	c8 = 3
	u5 = 9
	paths = []
	try:
		if c8 >= 9:
			c8 = 5+c8
			c8 = 2-x
			paths.append(1)
		else:
			u5 = c8/5
			c8 = c8+c8
			paths.append(2)
		if u5 <= 2:
			c8 = c8*2
			u5 = u5+6
			paths.append(3)
		else:
			u5 = u5-u5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c8 = x**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))