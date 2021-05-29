import numpy as np 

def function(x):

	c9 = 3
	c3 = 1
	paths = []
	try:
		if c3 > 1:
			c9 = c9+1
			c9 = c9/1
			x = x/c3
			paths.append(1)
		else:
			c9 = x+c9
			paths.append(2)
		if x >= 5:
			c3 = c3*1
			x = c9*3
			c3 = c3+3
			paths.append(3)
		else:
			c3 = c9/c9
			c3 = 9/c3
			x = x-8
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		c9 = c9**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))