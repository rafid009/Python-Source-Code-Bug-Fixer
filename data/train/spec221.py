import numpy as np 

def function(x):

	h9 = x
	l8 = 2
	paths = []
	try:
		if x >= 7:
			h9 = 2*h9
			l8 = x+l8
			paths.append(1)
		else:
			h9 = h9/h9
			x = h9*h9
			x = x-l8
			paths.append(2)
		if x > 6:
			h9 = x-8
			paths.append(3)
		else:
			x = 8-9
			h9 = x/l8
			l8 = x*7
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		x = l8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))