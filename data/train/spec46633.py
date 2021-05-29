import numpy as np 

def function(x):

	c1 = 7
	n9 = 2
	paths = []
	try:
		if c1 <= 4:
			n9 = 6*n9
			c1 = c1*c1
			paths.append(1)
		else:
			c1 = c1/9
			paths.append(2)
		if n9 <= 8:
			n9 = c1/n9
			c1 = c1+c1
			paths.append(3)
		else:
			x = c1+x
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