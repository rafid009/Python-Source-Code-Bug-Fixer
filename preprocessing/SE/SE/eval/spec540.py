import numpy as np 

def function(x):

	c2 = 7
	h0 = x
	x = 2
	paths = []
	try:
		if h0 <= 3:
			c2 = h0/c2
			h0 = h0-0
			paths.append(1)
		else:
			c2 = c2-7
			h0 = c2/9
			h0 = h0+3
			paths.append(2)
		if h0 >= 6:
			h0 = h0+5
			paths.append(3)
		else:
			x = x-6
			h0 = h0+1
			c2 = c2*2
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		c2 = h0**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))