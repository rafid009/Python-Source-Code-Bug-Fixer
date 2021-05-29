import numpy as np 

def function(x):

	b0 = 5
	c7 = 9
	paths = []
	try:
		if x <= 9:
			b0 = x*4
			x = x+b0
			c7 = 9*8
			paths.append(1)
		else:
			x = 1-x
			b0 = 7-b0
			paths.append(2)
		if x <= 7:
			x = 2-9
			paths.append(3)
		else:
			c7 = x-b0
			b0 = 3-c7
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		c7 = b0**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))