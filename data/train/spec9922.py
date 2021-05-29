import numpy as np 

def function(x):

	c4 = 9
	h4 = x
	paths = []
	try:
		if c4 <= 3:
			c4 = c4/7
			c4 = c4-1
			paths.append(1)
		else:
			x = h4/4
			h4 = 0-h4
			h4 = h4+4
			paths.append(2)
		if c4 > 3:
			c4 = 0-c4
			x = 1+x
			x = 8*x
			paths.append(3)
		else:
			x = 0/x
			x = 5-x
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		h4 = h4**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))