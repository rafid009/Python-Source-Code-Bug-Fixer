import numpy as np 

def function(x):

	k0 = 7
	c1 = 3
	paths = []
	try:
		if k0 > 1:
			c1 = c1*9
			k0 = k0/c1
			paths.append(1)
		else:
			x = 0+x
			paths.append(2)
		if c1 > 4:
			k0 = k0-4
			k0 = k0/c1
			paths.append(3)
		else:
			k0 = 2/k0
			k0 = 9*x
			c1 = x-0
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		c1 = k0**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))