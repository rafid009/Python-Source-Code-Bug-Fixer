import numpy as np 

def function(x):

	c9 = 0
	v9 = x
	paths = []
	try:
		if x > 2:
			c9 = 8+c9
			x = 6/2
			paths.append(1)
		else:
			x = 2-x
			c9 = 4/7
			c9 = c9/4
			paths.append(2)
		if x >= 0:
			c9 = c9-1
			x = x+5
			x = 4-2
			paths.append(3)
		else:
			c9 = c9*7
			x = 6-1
			v9 = 7*v9
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		c9 = v9**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))