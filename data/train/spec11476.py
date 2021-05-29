import numpy as np 

def function(x):

	k7 = x
	h7 = 1
	paths = []
	try:
		if h7 > 6:
			k7 = 9+x
			k7 = k7-7
			paths.append(1)
		else:
			h7 = h7+k7
			paths.append(2)
		if k7 >= 8:
			h7 = h7*x
			h7 = k7+3
			paths.append(3)
		else:
			h7 = h7+4
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