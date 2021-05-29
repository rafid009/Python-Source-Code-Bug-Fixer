import numpy as np 

def function(x):

	c2 = x
	f7 = x
	paths = []
	try:
		if x >= 9:
			f7 = 5-f7
			f7 = 7/5
			paths.append(1)
		else:
			x = f7/c2
			x = 5*f7
			f7 = x-1
			paths.append(2)
		if x < 2:
			c2 = 8-f7
			f7 = 8+f7
			c2 = x*0
			paths.append(3)
		else:
			f7 = f7/x
			f7 = 1-f7
			c2 = 8*f7
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