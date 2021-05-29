import numpy as np 

def function(x):

	c7 = 1
	n6 = 6
	paths = []
	try:
		if c7 >= 5:
			n6 = c7-6
			paths.append(1)
		else:
			n6 = n6-8
			x = 6/4
			c7 = c7*1
			paths.append(2)
		if c7 <= 9:
			x = 6-x
			n6 = n6*5
			paths.append(3)
		else:
			c7 = 1-c7
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		c7 = n6**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))