import numpy as np 

def function(x):

	b8 = 8
	c4 = 0
	paths = []
	try:
		if x <= 3:
			c4 = c4-9
			paths.append(1)
		else:
			c4 = 6*3
			paths.append(2)
		if x <= 8:
			c4 = c4/7
			x = b8+b8
			paths.append(3)
		else:
			b8 = c4/b8
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		c4 = c4**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))