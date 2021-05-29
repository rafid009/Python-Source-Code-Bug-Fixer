import numpy as np 

def function(x):

	h1 = x
	c4 = x
	paths = []
	try:
		if c4 > 6:
			c4 = 6/4
			h1 = 9*h1
			paths.append(1)
		else:
			x = x-5
			paths.append(2)
		if x <= 3:
			x = 4+x
			x = 3+x
			x = x+3
			paths.append(3)
		else:
			x = x*6
			c4 = x-2
			h1 = h1*8
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