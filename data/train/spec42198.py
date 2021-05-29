import numpy as np 

def function(x):

	k3 = 2
	c0 = 5
	paths = []
	try:
		if k3 <= 6:
			k3 = k3-7
			c0 = c0+3
			c0 = k3+c0
			paths.append(1)
		else:
			k3 = k3*5
			paths.append(2)
		if k3 > 4:
			x = x+3
			x = x+x
			x = c0+4
			paths.append(3)
		else:
			x = c0-5
			x = x/3
			k3 = 9-k3
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