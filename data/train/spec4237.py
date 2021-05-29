import numpy as np 

def function(x):

	h5 = 5
	c8 = x
	x = x
	paths = []
	try:
		if x <= 1:
			h5 = 4/x
			c8 = 8+h5
			x = 9-9
			paths.append(1)
		else:
			c8 = x+5
			x = x*8
			paths.append(2)
		if c8 > 8:
			c8 = c8-c8
			h5 = h5/5
			h5 = h5+7
			paths.append(3)
		else:
			h5 = 1*h5
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		h5 = h5**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))