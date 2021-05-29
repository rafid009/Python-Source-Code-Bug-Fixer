import numpy as np 

def function(x):

	h4 = x
	c3 = 8
	paths = []
	try:
		if c3 < 4:
			x = x/x
			paths.append(1)
		else:
			x = c3+x
			h4 = h4-1
			paths.append(2)
		if x > 6:
			x = x+3
			paths.append(3)
		else:
			h4 = x-c3
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