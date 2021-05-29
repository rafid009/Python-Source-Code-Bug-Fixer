import numpy as np 

def function(x):

	c6 = 5
	i9 = 1
	paths = []
	try:
		if i9 > 9:
			c6 = c6*i9
			x = 4+x
			paths.append(1)
		else:
			i9 = i9/9
			i9 = 5*x
			c6 = c6+8
			paths.append(2)
		if i9 < 3:
			x = i9*5
			paths.append(3)
		else:
			i9 = 4+i9
			i9 = 8/8
			x = 6/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c6 = x**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))