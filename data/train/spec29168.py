import numpy as np 

def function(x):

	n7 = x
	c1 = 1
	paths = []
	try:
		if x > 9:
			n7 = 8-1
			n7 = n7+5
			paths.append(1)
		else:
			c1 = c1-1
			c1 = c1/4
			x = 1+x
			paths.append(2)
		if x > 4:
			c1 = 6-9
			x = 6/x
			c1 = c1*n7
			paths.append(3)
		else:
			c1 = 5*7
			n7 = n7/6
			c1 = 2/c1
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		c1 = n7**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))