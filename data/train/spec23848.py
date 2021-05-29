import numpy as np 

def function(x):

	c7 = 5
	h6 = x
	paths = []
	try:
		if x > 3:
			c7 = c7/2
			paths.append(1)
		else:
			c7 = 3-c7
			paths.append(2)
		if h6 < 1:
			c7 = 2/c7
			h6 = h6/9
			h6 = x+8
			paths.append(3)
		else:
			x = 9*9
			x = h6+x
			h6 = h6+h6
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		x = c7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))