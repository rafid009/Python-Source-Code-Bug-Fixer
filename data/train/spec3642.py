import numpy as np 

def function(x):

	p1 = 1
	c0 = x
	x = 1
	paths = []
	try:
		if c0 > 8:
			p1 = p1+6
			paths.append(1)
		else:
			x = x/x
			paths.append(2)
		if x < 5:
			c0 = 9-c0
			p1 = 0-7
			paths.append(3)
		else:
			x = x/1
			c0 = 3-c0
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		c0 = p1**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))