import numpy as np 

def function(x):

	c1 = x
	r9 = 2
	paths = []
	try:
		if r9 > 2:
			c1 = c1+6
			paths.append(1)
		else:
			r9 = 7/r9
			x = 5+8
			r9 = 9*8
			paths.append(2)
		if c1 < 6:
			c1 = c1+c1
			paths.append(3)
		else:
			c1 = r9+c1
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		c1 = c1**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))