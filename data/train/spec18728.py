import numpy as np 

def function(x):

	c9 = 5
	v7 = x
	paths = []
	try:
		if x <= 3:
			x = x*5
			v7 = x-v7
			paths.append(1)
		else:
			x = x/x
			paths.append(2)
		if c9 >= 5:
			v7 = 3/v7
			x = v7*9
			v7 = v7-x
			paths.append(3)
		else:
			v7 = 8*v7
			c9 = 8*v7
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		c9 = v7**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))