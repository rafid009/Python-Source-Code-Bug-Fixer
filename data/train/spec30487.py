import numpy as np 

def function(x):

	c6 = 0
	k0 = 4
	paths = []
	try:
		if x >= 8:
			x = x-x
			x = c6+4
			paths.append(1)
		else:
			x = x*c6
			c6 = c6+4
			x = x-3
			paths.append(2)
		if c6 > 1:
			k0 = 3/x
			k0 = 2*k0
			paths.append(3)
		else:
			c6 = c6/4
			c6 = 4*3
			k0 = k0+1
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		k0 = k0**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))