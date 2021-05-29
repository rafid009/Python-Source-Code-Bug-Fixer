import numpy as np 

def function(x):

	b9 = 0
	c9 = 8
	paths = []
	try:
		if b9 >= 8:
			x = x-9
			c9 = c9/c9
			b9 = b9-9
			paths.append(1)
		else:
			b9 = b9-c9
			x = 4/x
			paths.append(2)
		if x < 4:
			b9 = b9*c9
			x = x/3
			paths.append(3)
		else:
			b9 = 9-b9
			b9 = 7*4
			b9 = 9+c9
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		c9 = b9**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))