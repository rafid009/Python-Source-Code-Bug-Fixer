import numpy as np 

def function(x):

	c9 = 0
	f9 = 3
	paths = []
	try:
		if c9 <= 8:
			f9 = f9*x
			x = x+8
			f9 = f9-x
			paths.append(1)
		else:
			f9 = f9-1
			f9 = 9/2
			paths.append(2)
		if c9 >= 3:
			c9 = c9/2
			f9 = 6-8
			c9 = 9/c9
			paths.append(3)
		else:
			x = x*x
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		c9 = f9**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))