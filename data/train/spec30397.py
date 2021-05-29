import numpy as np 

def function(x):

	c9 = x
	t4 = x
	x = 1
	paths = []
	try:
		if x <= 2:
			x = x/x
			paths.append(1)
		else:
			c9 = c9*8
			t4 = c9-t4
			paths.append(2)
		if c9 < 0:
			c9 = 6-c9
			c9 = 4-c9
			x = 6/7
			paths.append(3)
		else:
			c9 = 1*c9
			c9 = 2/x
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		c9 = t4**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))