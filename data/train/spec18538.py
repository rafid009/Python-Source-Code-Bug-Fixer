import numpy as np 

def function(x):

	c1 = 8
	c0 = x
	x = 2
	paths = []
	try:
		if x > 9:
			c1 = 3+c1
			paths.append(1)
		else:
			x = x+8
			c1 = 6/7
			paths.append(2)
		if c1 <= 7:
			x = 8*x
			paths.append(3)
		else:
			x = 4*x
			x = 8/c1
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		c0 = c0**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))