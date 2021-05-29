import numpy as np 

def function(x):

	n8 = 8
	c3 = 9
	paths = []
	try:
		if c3 > 2:
			c3 = 3-c3
			x = n8/x
			n8 = n8/6
			paths.append(1)
		else:
			n8 = 5-n8
			paths.append(2)
		if c3 < 9:
			c3 = 9/c3
			x = c3-9
			paths.append(3)
		else:
			x = 2-c3
			c3 = n8+n8
			x = 8*4
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		c3 = c3**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))