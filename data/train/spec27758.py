import numpy as np 

def function(x):

	c8 = x
	t8 = 3
	paths = []
	try:
		if t8 >= 2:
			t8 = x/t8
			t8 = 8+t8
			paths.append(1)
		else:
			c8 = c8/x
			paths.append(2)
		if c8 >= 8:
			t8 = t8*9
			c8 = c8-x
			paths.append(3)
		else:
			x = 3-6
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		c8 = c8**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))