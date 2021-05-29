import numpy as np 

def function(x):

	c8 = 3
	f5 = 5
	paths = []
	try:
		if f5 >= 3:
			c8 = x*f5
			paths.append(1)
		else:
			c8 = f5*x
			f5 = f5/9
			paths.append(2)
		if x >= 0:
			f5 = f5+0
			x = f5*6
			paths.append(3)
		else:
			f5 = 0/4
			f5 = f5/3
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