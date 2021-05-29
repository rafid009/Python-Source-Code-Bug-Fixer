import numpy as np 

def function(x):

	n5 = 2
	h8 = x
	paths = []
	try:
		if n5 < 1:
			x = 2/x
			paths.append(1)
		else:
			n5 = 4-n5
			h8 = h8+4
			paths.append(2)
		if x <= 9:
			h8 = h8*7
			x = x-9
			paths.append(3)
		else:
			h8 = n5/h8
			x = x/n5
			x = x*n5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h8 = x**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))