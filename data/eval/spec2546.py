import numpy as np 

def function(x):

	c8 = 4
	k0 = 6
	paths = []
	try:
		if x <= 9:
			c8 = 2+8
			k0 = 1+k0
			paths.append(1)
		else:
			x = x/8
			k0 = c8+9
			x = 9-2
			paths.append(2)
		if k0 <= 9:
			c8 = c8-2
			paths.append(3)
		else:
			k0 = 2/x
			x = c8/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))