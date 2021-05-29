import numpy as np 

def function(x):

	c5 = 5
	h8 = x
	paths = []
	try:
		if x >= 9:
			h8 = c5+h8
			x = x+5
			paths.append(1)
		else:
			x = 5/4
			c5 = h8*c5
			h8 = h8+c5
			paths.append(2)
		if x <= 4:
			h8 = 5*2
			x = 5-x
			x = 9/x
			paths.append(3)
		else:
			x = 8-9
			c5 = c5-2
			h8 = h8+h8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))