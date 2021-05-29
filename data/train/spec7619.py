import numpy as np 

def function(x):

	h0 = x
	h5 = 7
	paths = []
	try:
		if x > 2:
			h5 = 9-h0
			paths.append(1)
		else:
			h5 = 6+h5
			x = x+6
			x = 3/4
			paths.append(2)
		if h5 <= 0:
			h0 = 4*8
			paths.append(3)
		else:
			x = x/h0
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		h5 = h5**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))