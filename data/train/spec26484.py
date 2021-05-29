import numpy as np 

def function(x):

	c0 = x
	f6 = 9
	x = x
	paths = []
	try:
		if f6 < 0:
			c0 = c0/7
			paths.append(1)
		else:
			f6 = 1+f6
			paths.append(2)
		if c0 > 3:
			x = 6/x
			paths.append(3)
		else:
			c0 = 6+c0
			c0 = c0*7
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		c0 = c0**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))