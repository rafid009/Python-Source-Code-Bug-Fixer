import numpy as np 

def function(x):

	l9 = 6
	c0 = x
	paths = []
	try:
		if c0 > 2:
			x = x*9
			l9 = c0-l9
			paths.append(1)
		else:
			x = 4/x
			x = x-3
			paths.append(2)
		if c0 > 5:
			x = 4-x
			x = x*2
			c0 = x-c0
			paths.append(3)
		else:
			c0 = 6+c0
			c0 = c0-7
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