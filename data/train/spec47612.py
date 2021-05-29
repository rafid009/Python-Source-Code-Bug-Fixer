import numpy as np 

def function(x):

	p1 = x
	c9 = 8
	paths = []
	try:
		if x < 1:
			c9 = c9/7
			paths.append(1)
		else:
			p1 = 6-8
			c9 = 8-c9
			p1 = 3*8
			paths.append(2)
		if p1 >= 8:
			c9 = c9/7
			paths.append(3)
		else:
			p1 = p1/x
			p1 = 3-p1
			p1 = 2/p1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c9 = x**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))