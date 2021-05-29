import numpy as np 

def function(x):

	h0 = x
	c1 = 7
	paths = []
	try:
		if h0 > 6:
			x = x-x
			paths.append(1)
		else:
			c1 = c1-c1
			c1 = 3+x
			paths.append(2)
		if c1 > 2:
			h0 = 6-c1
			h0 = h0/2
			c1 = c1*4
			paths.append(3)
		else:
			x = 8+3
			c1 = c1-6
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		x = c1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))