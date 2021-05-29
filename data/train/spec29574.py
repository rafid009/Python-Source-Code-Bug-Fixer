import numpy as np 

def function(x):

	n2 = 4
	h7 = 9
	paths = []
	try:
		if x >= 2:
			h7 = h7+h7
			n2 = n2/5
			x = x-h7
			paths.append(1)
		else:
			h7 = 7-h7
			paths.append(2)
		if h7 <= 4:
			n2 = h7+8
			n2 = n2/7
			paths.append(3)
		else:
			h7 = h7-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h7 = x**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))