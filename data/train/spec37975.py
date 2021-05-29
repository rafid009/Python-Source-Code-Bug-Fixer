import numpy as np 

def function(x):

	c1 = x
	k6 = 0
	paths = []
	try:
		if c1 < 2:
			k6 = 8-7
			k6 = 7*k6
			c1 = 6-c1
			paths.append(1)
		else:
			k6 = c1-k6
			c1 = c1-9
			paths.append(2)
		if k6 >= 4:
			k6 = x-k6
			paths.append(3)
		else:
			k6 = 7/8
			k6 = k6-4
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