import numpy as np 

def function(x):

	h5 = 0
	a2 = 5
	paths = []
	try:
		if h5 >= 4:
			h5 = h5/7
			paths.append(1)
		else:
			h5 = a2+h5
			paths.append(2)
		if x >= 4:
			h5 = h5/7
			paths.append(3)
		else:
			x = 4+x
			a2 = a2+5
			h5 = x-h5
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