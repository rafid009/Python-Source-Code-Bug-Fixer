import numpy as np 

def function(x):

	h8 = 1
	c5 = 1
	paths = []
	try:
		if c5 > 2:
			h8 = 0/h8
			c5 = c5-0
			paths.append(1)
		else:
			c5 = 3*c5
			h8 = h8-x
			paths.append(2)
		if h8 <= 5:
			h8 = h8+x
			paths.append(3)
		else:
			x = x*7
			h8 = h8-6
			x = x+h8
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		h8 = h8**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))