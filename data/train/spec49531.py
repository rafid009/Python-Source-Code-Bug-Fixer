import numpy as np 

def function(x):

	t0 = x
	c3 = x
	x = 7
	paths = []
	try:
		if c3 > 6:
			t0 = 7*9
			paths.append(1)
		else:
			c3 = c3*6
			paths.append(2)
		if c3 < 7:
			t0 = t0*x
			paths.append(3)
		else:
			c3 = 6/5
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		c3 = t0**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))