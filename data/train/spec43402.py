import numpy as np 

def function(x):

	c4 = 6
	w7 = x
	paths = []
	try:
		if c4 >= 6:
			c4 = c4-x
			c4 = 1-8
			paths.append(1)
		else:
			c4 = c4+c4
			paths.append(2)
		if x <= 9:
			w7 = x+6
			c4 = c4/3
			paths.append(3)
		else:
			c4 = w7-x
			c4 = c4/7
			c4 = c4/w7
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		c4 = c4**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))