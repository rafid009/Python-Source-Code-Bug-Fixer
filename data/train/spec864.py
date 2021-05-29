import numpy as np 

def function(x):

	c0 = 1
	i9 = x
	paths = []
	try:
		if x >= 8:
			x = 4/x
			x = x*0
			paths.append(1)
		else:
			x = 9/x
			i9 = 9/i9
			paths.append(2)
		if x > 5:
			i9 = 4*i9
			paths.append(3)
		else:
			c0 = c0+c0
			i9 = i9*9
			c0 = 6/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c0 = x**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))