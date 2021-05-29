import numpy as np 

def function(x):

	c7 = 4
	h4 = x
	paths = []
	try:
		if c7 > 7:
			c7 = 8-5
			x = 8/h4
			paths.append(1)
		else:
			c7 = c7-x
			c7 = 9*6
			paths.append(2)
		if x >= 6:
			c7 = 8*4
			h4 = h4+7
			c7 = c7*5
			paths.append(3)
		else:
			c7 = c7*2
			x = x*x
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		x = h4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))