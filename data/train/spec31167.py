import numpy as np 

def function(x):

	f8 = x
	c0 = x
	paths = []
	try:
		if c0 > 5:
			x = 3*x
			f8 = f8-f8
			x = x*f8
			paths.append(1)
		else:
			x = x/4
			c0 = c0/4
			paths.append(2)
		if x <= 5:
			x = x/8
			paths.append(3)
		else:
			c0 = c0+1
			f8 = 1*f8
			x = 6-x
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