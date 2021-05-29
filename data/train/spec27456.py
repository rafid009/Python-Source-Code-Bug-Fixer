import numpy as np 

def function(x):

	f4 = x
	c6 = x
	paths = []
	try:
		if x >= 0:
			x = 0*x
			x = x+1
			paths.append(1)
		else:
			f4 = f4-c6
			paths.append(2)
		if f4 < 2:
			f4 = x+f4
			f4 = x*f4
			x = x/f4
			paths.append(3)
		else:
			c6 = 3/f4
			x = x+f4
			x = x-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c6 = x**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))