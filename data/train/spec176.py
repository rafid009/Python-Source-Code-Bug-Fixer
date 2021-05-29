import numpy as np 

def function(x):

	h5 = 1
	b7 = 7
	paths = []
	try:
		if h5 >= 0:
			h5 = 3/h5
			paths.append(1)
		else:
			b7 = x*b7
			paths.append(2)
		if b7 < 8:
			b7 = x+h5
			b7 = b7-9
			paths.append(3)
		else:
			b7 = x*8
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		h5 = b7**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))