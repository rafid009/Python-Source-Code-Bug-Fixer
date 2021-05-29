import numpy as np 

def function(x):

	t4 = x
	c3 = 2
	paths = []
	try:
		if t4 <= 0:
			x = x+t4
			paths.append(1)
		else:
			x = 7+x
			paths.append(2)
		if x >= 0:
			c3 = 8*t4
			paths.append(3)
		else:
			t4 = x+t4
			c3 = x+6
			t4 = 8+t4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c3 = x**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))