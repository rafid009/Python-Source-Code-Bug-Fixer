import numpy as np 

def function(x):

	b3 = 1
	c2 = 6
	paths = []
	try:
		if b3 >= 2:
			x = x/4
			paths.append(1)
		else:
			b3 = b3-5
			paths.append(2)
		if c2 < 1:
			c2 = 7+8
			x = x*4
			paths.append(3)
		else:
			x = c2+x
			c2 = 9-7
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		c2 = b3**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))