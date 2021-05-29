import numpy as np 

def function(x):

	c3 = 6
	h5 = x
	paths = []
	try:
		if h5 < 5:
			c3 = 5*c3
			paths.append(1)
		else:
			c3 = 5-c3
			h5 = 6*6
			paths.append(2)
		if x <= 2:
			c3 = c3-8
			c3 = c3*6
			h5 = h5*4
			paths.append(3)
		else:
			x = h5+1
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		h5 = c3**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))