import numpy as np 

def function(x):

	c0 = x
	c4 = 2
	paths = []
	try:
		if c0 < 2:
			x = x-1
			c0 = x*5
			paths.append(1)
		else:
			c0 = 6/c4
			c0 = 8-c0
			paths.append(2)
		if c4 > 5:
			x = c4/7
			c0 = 6+1
			paths.append(3)
		else:
			c4 = 3-4
			c0 = x/4
			c0 = c0-3
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		x = c4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))