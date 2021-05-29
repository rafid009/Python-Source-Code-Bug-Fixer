import numpy as np 

def function(x):

	c4 = 4
	i9 = x
	paths = []
	try:
		if x >= 8:
			i9 = i9/c4
			paths.append(1)
		else:
			i9 = i9+7
			x = x*6
			c4 = 9+c4
			paths.append(2)
		if i9 < 1:
			c4 = 3-5
			paths.append(3)
		else:
			x = 7-4
			c4 = 9*i9
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