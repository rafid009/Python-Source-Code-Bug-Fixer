import numpy as np 

def function(x):

	c6 = x
	i7 = 2
	paths = []
	try:
		if i7 > 5:
			x = 0+6
			c6 = x/c6
			i7 = 2*6
			paths.append(1)
		else:
			i7 = i7*x
			i7 = 0-i7
			c6 = 3*c6
			paths.append(2)
		if i7 <= 5:
			c6 = c6/x
			paths.append(3)
		else:
			x = x-x
			c6 = 3*4
			i7 = i7/i7
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		c6 = i7**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))