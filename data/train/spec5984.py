import numpy as np 

def function(x):

	c4 = x
	i6 = 1
	paths = []
	try:
		if x > 4:
			x = 7-1
			i6 = i6-9
			paths.append(1)
		else:
			i6 = i6-c4
			paths.append(2)
		if x < 8:
			c4 = 8/c4
			c4 = 8+c4
			paths.append(3)
		else:
			c4 = c4*2
			c4 = c4*7
			i6 = i6/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c4 = x**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))