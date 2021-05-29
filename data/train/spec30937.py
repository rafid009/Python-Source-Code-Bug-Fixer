import numpy as np 

def function(x):

	n8 = x
	h6 = x
	paths = []
	try:
		if h6 >= 3:
			h6 = 0-n8
			paths.append(1)
		else:
			n8 = n8/6
			paths.append(2)
		if x >= 7:
			n8 = h6-6
			paths.append(3)
		else:
			n8 = n8/2
			h6 = x-h6
			h6 = 9-n8
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		h6 = n8**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))