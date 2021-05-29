import numpy as np 

def function(x):

	x4 = 9
	c5 = x
	paths = []
	try:
		if x < 6:
			c5 = c5/x
			c5 = 7-8
			paths.append(1)
		else:
			c5 = x+c5
			x4 = x4*5
			x4 = x4-3
			paths.append(2)
		if x < 3:
			x4 = x4-x4
			paths.append(3)
		else:
			x4 = c5*4
			x4 = x4-x
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