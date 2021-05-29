import numpy as np 

def function(x):

	h5 = x
	q6 = 0
	paths = []
	try:
		if q6 > 2:
			q6 = 9-2
			h5 = 7*0
			paths.append(1)
		else:
			h5 = h5/8
			paths.append(2)
		if h5 < 1:
			q6 = 9+1
			paths.append(3)
		else:
			q6 = q6/7
			h5 = x-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h5 = x**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))