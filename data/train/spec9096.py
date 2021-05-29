import numpy as np 

def function(x):

	c4 = 8
	h2 = x
	paths = []
	try:
		if x < 7:
			c4 = c4+2
			c4 = c4/9
			paths.append(1)
		else:
			c4 = 1-3
			c4 = c4*6
			h2 = 5-c4
			paths.append(2)
		if c4 <= 3:
			h2 = 4/h2
			paths.append(3)
		else:
			c4 = x/7
			h2 = 7/h2
			x = 7+3
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