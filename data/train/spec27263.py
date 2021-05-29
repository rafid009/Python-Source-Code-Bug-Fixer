import numpy as np 

def function(x):

	c6 = x
	h0 = 7
	paths = []
	try:
		if h0 < 8:
			c6 = c6/5
			paths.append(1)
		else:
			c6 = c6*1
			paths.append(2)
		if x >= 4:
			x = 8/x
			paths.append(3)
		else:
			h0 = 5/c6
			h0 = h0+7
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		c6 = c6**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))