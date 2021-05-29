import numpy as np 

def function(x):

	h2 = 8
	c0 = 4
	paths = []
	try:
		if x < 5:
			h2 = h2+c0
			paths.append(1)
		else:
			c0 = 3+h2
			paths.append(2)
		if x >= 3:
			c0 = c0/5
			paths.append(3)
		else:
			c0 = c0/9
			c0 = 3-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h2 = x**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))