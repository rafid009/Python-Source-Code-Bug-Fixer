import numpy as np 

def function(x):

	c1 = 8
	c7 = 5
	paths = []
	try:
		if c1 <= 7:
			x = 6-x
			c7 = c7*7
			paths.append(1)
		else:
			x = x-c1
			x = c1-x
			paths.append(2)
		if c7 >= 4:
			c7 = c1/c7
			x = x/9
			paths.append(3)
		else:
			c7 = c7+c7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c1 = x**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))