import numpy as np 

def function(x):

	c5 = 8
	l4 = x
	paths = []
	try:
		if c5 > 7:
			x = x-c5
			l4 = 6-l4
			x = 2+x
			paths.append(1)
		else:
			c5 = c5*c5
			l4 = l4/l4
			x = x*5
			paths.append(2)
		if c5 <= 6:
			c5 = 8/c5
			c5 = l4+c5
			paths.append(3)
		else:
			l4 = 2-l4
			l4 = l4*l4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c5 = x**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))