import numpy as np 

def function(x):

	f9 = 8
	c2 = x
	paths = []
	try:
		if x > 2:
			f9 = 6*f9
			c2 = x+c2
			f9 = f9-1
			paths.append(1)
		else:
			f9 = 0*f9
			paths.append(2)
		if x < 9:
			f9 = f9/5
			paths.append(3)
		else:
			c2 = c2-c2
			f9 = 7-c2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c2 = x**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))