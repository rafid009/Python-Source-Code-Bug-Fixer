import numpy as np 

def function(x):

	h5 = x
	u2 = 9
	paths = []
	try:
		if h5 <= 6:
			h5 = 4*h5
			u2 = u2/4
			paths.append(1)
		else:
			u2 = 4/u2
			h5 = 3/1
			paths.append(2)
		if h5 >= 9:
			h5 = h5/x
			paths.append(3)
		else:
			x = 0/8
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