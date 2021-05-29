import numpy as np 

def function(x):

	h3 = x
	c0 = x
	paths = []
	try:
		if x >= 8:
			h3 = h3/1
			x = x*9
			paths.append(1)
		else:
			x = h3+x
			x = 5-x
			x = c0+7
			paths.append(2)
		if x >= 2:
			c0 = 4*c0
			c0 = h3+5
			h3 = h3+5
			paths.append(3)
		else:
			x = x*2
			x = c0/7
			c0 = 0*c0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h3 = x**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))