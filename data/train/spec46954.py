import numpy as np 

def function(x):

	x5 = 9
	h9 = 5
	paths = []
	try:
		if x5 < 5:
			x5 = h9*4
			x5 = x5+4
			x5 = 3+x5
			paths.append(1)
		else:
			x5 = h9*x5
			x5 = 4*x
			h9 = x5+x5
			paths.append(2)
		if h9 >= 3:
			h9 = h9/5
			paths.append(3)
		else:
			x5 = 1*0
			h9 = x-x
			x5 = x5+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h9 = x**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))