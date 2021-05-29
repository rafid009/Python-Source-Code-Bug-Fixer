import numpy as np 

def function(x):

	i0 = 9
	c7 = 8
	paths = []
	try:
		if x > 9:
			i0 = 9+0
			i0 = 3-i0
			paths.append(1)
		else:
			c7 = 0-7
			c7 = 4-6
			paths.append(2)
		if c7 > 5:
			c7 = x+c7
			i0 = i0-c7
			c7 = c7+i0
			paths.append(3)
		else:
			c7 = 9/c7
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		c7 = c7**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))