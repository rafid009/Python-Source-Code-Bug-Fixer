import numpy as np 

def function(x):

	c0 = 2
	k5 = x
	paths = []
	try:
		if c0 <= 3:
			c0 = c0+4
			k5 = x/8
			k5 = k5+k5
			paths.append(1)
		else:
			k5 = k5*7
			x = 7+3
			x = k5*c0
			paths.append(2)
		if x <= 9:
			k5 = k5-2
			c0 = c0*k5
			paths.append(3)
		else:
			c0 = c0-9
			c0 = 5-2
			x = x+c0
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