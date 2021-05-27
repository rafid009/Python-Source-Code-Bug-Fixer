import numpy as np 

def function(x):

	h5 = x
	c5 = 7
	paths = []
	try:
		if c5 > 9:
			c5 = x*1
			paths.append(1)
		else:
			h5 = h5*h5
			paths.append(2)
		if h5 < 7:
			x = 6-4
			paths.append(3)
		else:
			h5 = x/h5
			h5 = c5*x
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		x = h5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))