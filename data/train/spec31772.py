import numpy as np 

def function(x):

	c7 = 1
	n1 = 1
	paths = []
	try:
		if c7 < 1:
			n1 = n1/9
			paths.append(1)
		else:
			x = x/5
			c7 = c7-8
			n1 = 0/6
			paths.append(2)
		if c7 <= 1:
			n1 = 4-1
			x = x/3
			paths.append(3)
		else:
			n1 = 1/9
			n1 = 5/c7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c7 = x**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))