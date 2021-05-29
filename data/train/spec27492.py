import numpy as np 

def function(x):

	c5 = x
	f6 = 6
	paths = []
	try:
		if x < 2:
			f6 = f6+f6
			f6 = 6-f6
			paths.append(1)
		else:
			x = x/f6
			f6 = x-f6
			c5 = 8/c5
			paths.append(2)
		if x >= 8:
			f6 = f6+f6
			paths.append(3)
		else:
			f6 = c5*x
			c5 = f6+9
			c5 = 2-f6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c5 = x**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))