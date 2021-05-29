import numpy as np 

def function(x):

	c3 = x
	t4 = 7
	paths = []
	try:
		if x <= 9:
			t4 = t4*4
			paths.append(1)
		else:
			t4 = 5/3
			x = t4*6
			paths.append(2)
		if c3 > 4:
			t4 = t4+c3
			t4 = c3+t4
			paths.append(3)
		else:
			c3 = c3*7
			t4 = x-8
			c3 = c3/x
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