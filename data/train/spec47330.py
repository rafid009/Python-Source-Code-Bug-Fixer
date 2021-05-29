import numpy as np 

def function(x):

	t5 = 6
	c0 = 6
	paths = []
	try:
		if x < 2:
			c0 = 6*6
			x = x/x
			t5 = 8-t5
			paths.append(1)
		else:
			c0 = 1-t5
			x = 2+t5
			x = 4/x
			paths.append(2)
		if c0 > 9:
			x = x-c0
			paths.append(3)
		else:
			t5 = 6-x
			t5 = 1/t5
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