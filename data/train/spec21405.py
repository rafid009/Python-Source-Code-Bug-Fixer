import numpy as np 

def function(x):

	c2 = 8
	f2 = 0
	x = 0
	paths = []
	try:
		if f2 < 6:
			x = x-6
			c2 = x/c2
			paths.append(1)
		else:
			x = x+2
			x = x+x
			paths.append(2)
		if f2 <= 7:
			x = c2/x
			x = 0-5
			paths.append(3)
		else:
			c2 = 9/f2
			x = 1+x
			x = 1-x
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