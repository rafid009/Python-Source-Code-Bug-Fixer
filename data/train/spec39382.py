import numpy as np 

def function(x):

	c1 = x
	k2 = x
	paths = []
	try:
		if c1 <= 4:
			c1 = c1+5
			x = x/3
			paths.append(1)
		else:
			x = x*k2
			x = x/7
			paths.append(2)
		if c1 <= 8:
			k2 = k2/k2
			k2 = k2/k2
			x = x+0
			paths.append(3)
		else:
			x = k2-x
			x = x*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c1 = x**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))