import numpy as np 

def function(x):

	c5 = x
	h4 = 7
	paths = []
	try:
		if h4 <= 5:
			c5 = h4/3
			paths.append(1)
		else:
			c5 = c5-3
			c5 = 1-c5
			paths.append(2)
		if h4 >= 8:
			h4 = h4+5
			h4 = h4/8
			x = 2*1
			paths.append(3)
		else:
			c5 = c5*h4
			x = 4-x
			c5 = c5*h4
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		x = c5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))