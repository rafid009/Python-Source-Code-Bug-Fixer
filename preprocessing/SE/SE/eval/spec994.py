import numpy as np 

def function(x):

	c6 = 5
	f5 = x
	paths = []
	try:
		if f5 >= 3:
			c6 = 4+c6
			c6 = c6+1
			paths.append(1)
		else:
			f5 = c6/9
			f5 = 0+f5
			c6 = 6+4
			paths.append(2)
		if f5 > 8:
			f5 = 5*f5
			x = c6/3
			paths.append(3)
		else:
			c6 = 1-8
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