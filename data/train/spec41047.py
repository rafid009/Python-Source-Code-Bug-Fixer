import numpy as np 

def function(x):

	c3 = 3
	t0 = 7
	paths = []
	try:
		if t0 >= 0:
			t0 = 9+t0
			paths.append(1)
		else:
			c3 = 8*c3
			x = 9+c3
			paths.append(2)
		if c3 >= 9:
			t0 = 8+t0
			c3 = 4/c3
			paths.append(3)
		else:
			t0 = x-0
			c3 = c3+c3
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