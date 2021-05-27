import numpy as np 

def function(x):

	h5 = x
	s8 = x
	paths = []
	try:
		if h5 >= 0:
			x = x-1
			h5 = 6-h5
			h5 = 1*h5
			paths.append(1)
		else:
			x = 5/9
			paths.append(2)
		if x > 5:
			x = s8*x
			x = 4*x
			x = 5+1
			paths.append(3)
		else:
			x = x+h5
			h5 = h5/s8
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		h5 = s8**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))