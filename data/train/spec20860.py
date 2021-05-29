import numpy as np 

def function(x):

	l4 = x
	c5 = x
	paths = []
	try:
		if c5 > 1:
			l4 = 6*l4
			x = x*3
			l4 = 4-l4
			paths.append(1)
		else:
			l4 = l4-l4
			c5 = 0*x
			paths.append(2)
		if x >= 8:
			l4 = l4-3
			c5 = c5-x
			paths.append(3)
		else:
			l4 = l4*9
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		c5 = c5**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))