import numpy as np 

def function(x):

	u9 = x
	c9 = 6
	paths = []
	try:
		if x < 9:
			u9 = 1+u9
			u9 = c9*7
			c9 = u9-c9
			paths.append(1)
		else:
			x = x+4
			c9 = 6*c9
			paths.append(2)
		if c9 <= 8:
			c9 = 7-2
			u9 = u9+u9
			paths.append(3)
		else:
			c9 = c9*x
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