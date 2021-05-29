import numpy as np 

def function(x):

	u0 = 4
	c7 = x
	paths = []
	try:
		if u0 <= 2:
			u0 = 8*9
			x = 5+0
			u0 = u0/u0
			paths.append(1)
		else:
			c7 = 5+c7
			u0 = x/1
			paths.append(2)
		if u0 > 5:
			x = x-c7
			x = 7/3
			paths.append(3)
		else:
			c7 = 1-4
			c7 = c7+2
			x = x/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c7 = x**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))