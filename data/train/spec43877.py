import numpy as np 

def function(x):

	c8 = 6
	b6 = 6
	paths = []
	try:
		if x <= 6:
			b6 = 7-3
			paths.append(1)
		else:
			x = x-4
			c8 = b6*b6
			b6 = b6-b6
			paths.append(2)
		if b6 > 3:
			c8 = 4*2
			b6 = b6-c8
			b6 = 6*b6
			paths.append(3)
		else:
			c8 = c8-7
			c8 = 6+c8
			c8 = 0+c8
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		c8 = b6**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))