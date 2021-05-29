import numpy as np 

def function(x):

	c7 = x
	t6 = x
	paths = []
	try:
		if c7 >= 4:
			c7 = c7-t6
			t6 = 5/x
			paths.append(1)
		else:
			x = 6+9
			paths.append(2)
		if t6 > 3:
			x = 0/6
			paths.append(3)
		else:
			x = c7*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c7 = x**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))