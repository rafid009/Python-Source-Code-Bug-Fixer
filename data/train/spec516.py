import numpy as np 

def function(x):

	h2 = 1
	c3 = 8
	paths = []
	try:
		if c3 <= 8:
			h2 = h2+x
			h2 = 5-h2
			c3 = 5/c3
			paths.append(1)
		else:
			c3 = 6/c3
			paths.append(2)
		if h2 >= 5:
			c3 = c3-8
			x = x*x
			h2 = 4*c3
			paths.append(3)
		else:
			c3 = 9-c3
			x = x*1
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		h2 = h2**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))