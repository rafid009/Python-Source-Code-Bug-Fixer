import numpy as np 

def function(x):

	c3 = 2
	i9 = x
	paths = []
	try:
		if i9 >= 9:
			x = 0-c3
			paths.append(1)
		else:
			x = 7/1
			paths.append(2)
		if i9 < 9:
			x = i9-0
			paths.append(3)
		else:
			i9 = 2/i9
			c3 = c3/9
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		c3 = i9**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))