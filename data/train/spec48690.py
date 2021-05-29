import numpy as np 

def function(x):

	c0 = 4
	u3 = x
	paths = []
	try:
		if x < 6:
			u3 = u3/c0
			u3 = u3+4
			x = x+x
			paths.append(1)
		else:
			c0 = u3*c0
			x = x+1
			c0 = 0-5
			paths.append(2)
		if c0 >= 3:
			c0 = c0+7
			paths.append(3)
		else:
			x = 0*x
			c0 = 5-c0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c0 = x**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))