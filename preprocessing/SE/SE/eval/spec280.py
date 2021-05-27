import numpy as np 

def function(x):

	h7 = 2
	c0 = x
	paths = []
	try:
		if h7 < 6:
			x = x*0
			h7 = c0-7
			paths.append(1)
		else:
			h7 = h7*9
			x = 7*x
			c0 = c0-c0
			paths.append(2)
		if h7 <= 0:
			x = 5-4
			paths.append(3)
		else:
			h7 = h7-x
			c0 = x+3
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		c0 = c0**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))