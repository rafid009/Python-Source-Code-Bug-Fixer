import numpy as np 

def function(x):

	h0 = x
	c6 = 4
	paths = []
	try:
		if c6 <= 2:
			h0 = 9+2
			paths.append(1)
		else:
			c6 = 7*c6
			paths.append(2)
		if x >= 7:
			h0 = h0-8
			c6 = c6/h0
			paths.append(3)
		else:
			x = x*5
			h0 = 2+h0
			h0 = x+x
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		x = h0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))