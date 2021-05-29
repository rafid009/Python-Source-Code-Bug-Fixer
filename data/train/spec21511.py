import numpy as np 

def function(x):

	h4 = x
	c5 = 4
	x = 1
	paths = []
	try:
		if c5 >= 7:
			x = 7/1
			x = 7/3
			paths.append(1)
		else:
			x = 6+4
			c5 = c5/2
			c5 = x/9
			paths.append(2)
		if h4 > 5:
			h4 = x*7
			paths.append(3)
		else:
			c5 = 8/c5
			c5 = 6+3
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		c5 = h4**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))