import numpy as np 

def function(x):

	c6 = 1
	t0 = 0
	paths = []
	try:
		if x <= 2:
			x = x-9
			paths.append(1)
		else:
			t0 = 8/3
			x = x-c6
			paths.append(2)
		if t0 <= 4:
			c6 = c6+t0
			t0 = x+x
			paths.append(3)
		else:
			x = 8+x
			c6 = 6*c6
			x = t0-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c6 = x**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))