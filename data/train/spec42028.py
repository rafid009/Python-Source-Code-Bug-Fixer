import numpy as np 

def function(x):

	c4 = 0
	t0 = x
	paths = []
	try:
		if c4 <= 6:
			t0 = x-t0
			c4 = 6+4
			paths.append(1)
		else:
			x = 0/x
			paths.append(2)
		if c4 > 2:
			t0 = 0*c4
			x = x-x
			c4 = t0-c4
			paths.append(3)
		else:
			t0 = 9*9
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		c4 = c4**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))