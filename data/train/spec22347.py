import numpy as np 

def function(x):

	h3 = x
	c0 = 2
	paths = []
	try:
		if h3 <= 2:
			c0 = c0-0
			h3 = h3+1
			paths.append(1)
		else:
			c0 = c0-x
			c0 = c0/5
			h3 = x*h3
			paths.append(2)
		if h3 >= 1:
			x = 1-x
			c0 = h3/c0
			c0 = c0+9
			paths.append(3)
		else:
			x = x+2
			c0 = 3/c0
			c0 = 5*6
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		h3 = h3**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))