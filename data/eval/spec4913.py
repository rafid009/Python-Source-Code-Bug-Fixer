import numpy as np 

def function(x):

	c4 = 3
	h7 = 2
	paths = []
	try:
		if h7 <= 0:
			h7 = h7+2
			paths.append(1)
		else:
			h7 = c4/7
			h7 = x+h7
			c4 = x*c4
			paths.append(2)
		if c4 > 5:
			c4 = 1+c4
			paths.append(3)
		else:
			h7 = h7-9
			h7 = h7+7
			h7 = h7*5
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		c4 = h7**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))