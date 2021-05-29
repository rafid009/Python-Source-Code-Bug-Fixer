import numpy as np 

def function(x):

	c8 = 1
	u0 = x
	paths = []
	try:
		if u0 >= 8:
			u0 = u0/3
			paths.append(1)
		else:
			x = c8+x
			paths.append(2)
		if u0 > 3:
			c8 = c8/c8
			c8 = 9+c8
			u0 = 1*u0
			paths.append(3)
		else:
			x = x*6
			x = x-2
			u0 = 5/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c8 = x**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))