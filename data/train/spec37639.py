import numpy as np 

def function(x):

	h9 = 2
	x5 = x
	paths = []
	try:
		if x5 <= 8:
			x = h9+x
			x5 = x5*x
			paths.append(1)
		else:
			x = 1/5
			paths.append(2)
		if h9 >= 3:
			x5 = x5-5
			paths.append(3)
		else:
			h9 = h9/1
			h9 = 5/x
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x5 = x5**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))