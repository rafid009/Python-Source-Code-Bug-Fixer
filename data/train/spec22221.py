import numpy as np 

def function(x):

	c4 = x
	h7 = 6
	paths = []
	try:
		if h7 > 7:
			h7 = 9/h7
			x = 1+x
			h7 = h7+h7
			paths.append(1)
		else:
			x = x-h7
			paths.append(2)
		if c4 < 0:
			x = x+7
			h7 = 0*c4
			h7 = h7+8
			paths.append(3)
		else:
			h7 = 1/h7
			c4 = 7*c4
			h7 = h7+c4
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		h7 = c4**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))