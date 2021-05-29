import numpy as np 

def function(x):

	x5 = x
	h9 = 7
	paths = []
	try:
		if x > 4:
			x = h9*x
			x = x-7
			paths.append(1)
		else:
			x5 = h9/x5
			x = 3/x
			paths.append(2)
		if x >= 2:
			h9 = h9/9
			h9 = 0-9
			x = 7/7
			paths.append(3)
		else:
			h9 = 5/3
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x = x5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))