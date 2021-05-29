import numpy as np 

def function(x):

	n1 = 0
	h9 = x
	paths = []
	try:
		if h9 > 1:
			n1 = 7-n1
			h9 = 7/h9
			paths.append(1)
		else:
			x = 7-x
			n1 = 9-2
			paths.append(2)
		if x <= 8:
			x = x-9
			paths.append(3)
		else:
			x = x+8
			n1 = h9+2
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		h9 = n1**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))