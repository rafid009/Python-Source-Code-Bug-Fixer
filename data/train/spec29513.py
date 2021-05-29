import numpy as np 

def function(x):

	h5 = x
	x4 = 2
	paths = []
	try:
		if h5 <= 4:
			h5 = h5-x
			paths.append(1)
		else:
			x = x-7
			x = x*x
			x = 9*5
			paths.append(2)
		if h5 > 9:
			x = h5*5
			x4 = x4+0
			x4 = x4-h5
			paths.append(3)
		else:
			h5 = x4-h5
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