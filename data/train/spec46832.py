import numpy as np 

def function(x):

	h8 = x
	c1 = 8
	paths = []
	try:
		if x >= 5:
			x = 1*6
			x = c1*5
			x = 7*8
			paths.append(1)
		else:
			h8 = x+6
			h8 = x*3
			paths.append(2)
		if h8 <= 3:
			x = 6+x
			c1 = 0-c1
			paths.append(3)
		else:
			c1 = x*x
			c1 = 5-c1
			h8 = c1/h8
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