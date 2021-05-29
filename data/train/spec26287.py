import numpy as np 

def function(x):

	h1 = x
	c4 = x
	paths = []
	try:
		if c4 < 8:
			c4 = 0+2
			c4 = h1+x
			paths.append(1)
		else:
			h1 = 1+h1
			c4 = 9+c4
			paths.append(2)
		if x < 3:
			c4 = c4+4
			paths.append(3)
		else:
			c4 = 1*c4
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		c4 = h1**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))