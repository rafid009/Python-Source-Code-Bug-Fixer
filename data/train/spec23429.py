import numpy as np 

def function(x):

	c0 = 6
	p6 = x
	paths = []
	try:
		if x > 9:
			x = 3*p6
			x = c0-4
			c0 = 4+c0
			paths.append(1)
		else:
			p6 = 5+p6
			paths.append(2)
		if p6 >= 5:
			x = x+8
			c0 = 1/8
			paths.append(3)
		else:
			p6 = p6+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c0 = x**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))