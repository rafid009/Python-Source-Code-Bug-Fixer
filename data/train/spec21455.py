import numpy as np 

def function(x):

	c5 = 0
	t8 = 3
	paths = []
	try:
		if x < 8:
			x = x-3
			c5 = 5/4
			x = 4-x
			paths.append(1)
		else:
			t8 = t8+t8
			paths.append(2)
		if x <= 0:
			t8 = 7*x
			c5 = 6/t8
			t8 = 7+c5
			paths.append(3)
		else:
			c5 = 9+c5
			c5 = 1-c5
			x = x/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c5 = x**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))