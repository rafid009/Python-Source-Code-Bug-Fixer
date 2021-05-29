import numpy as np 

def function(x):

	c1 = x
	f8 = 1
	paths = []
	try:
		if c1 <= 2:
			x = x-c1
			f8 = f8-4
			f8 = x*x
			paths.append(1)
		else:
			c1 = f8*3
			paths.append(2)
		if c1 < 6:
			f8 = x*f8
			paths.append(3)
		else:
			x = 5*x
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		c1 = c1**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))