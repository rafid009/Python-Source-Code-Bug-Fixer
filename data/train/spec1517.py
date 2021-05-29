import numpy as np 

def function(x):

	f6 = x
	c9 = x
	paths = []
	try:
		if f6 < 9:
			x = x+6
			paths.append(1)
		else:
			x = 1+7
			paths.append(2)
		if f6 >= 8:
			c9 = c9*7
			c9 = 3/c9
			c9 = 1-5
			paths.append(3)
		else:
			x = x-8
			c9 = 9+c9
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		c9 = f6**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))