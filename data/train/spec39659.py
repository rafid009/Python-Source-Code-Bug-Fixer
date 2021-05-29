import numpy as np 

def function(x):

	c4 = x
	h5 = x
	x = 9
	paths = []
	try:
		if c4 < 5:
			h5 = h5+4
			h5 = h5+6
			paths.append(1)
		else:
			c4 = c4-0
			c4 = c4+9
			paths.append(2)
		if h5 > 4:
			x = 9/x
			c4 = c4/3
			x = c4*2
			paths.append(3)
		else:
			x = x/x
			x = x/h5
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