import numpy as np 

def function(x):

	h5 = 1
	j6 = x
	paths = []
	try:
		if h5 > 3:
			h5 = 8+h5
			x = x+8
			paths.append(1)
		else:
			h5 = h5/4
			h5 = x+h5
			j6 = 8+j6
			paths.append(2)
		if j6 >= 2:
			h5 = 0*h5
			paths.append(3)
		else:
			j6 = j6-2
			h5 = h5-8
			h5 = h5/j6
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		h5 = j6**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))