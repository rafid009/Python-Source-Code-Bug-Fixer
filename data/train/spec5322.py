import numpy as np 

def function(x):

	u9 = 5
	h5 = 7
	paths = []
	try:
		if h5 >= 6:
			h5 = h5/x
			h5 = 9-h5
			paths.append(1)
		else:
			x = 4-x
			paths.append(2)
		if h5 <= 0:
			x = x-u9
			x = h5+1
			x = 1+x
			paths.append(3)
		else:
			x = 2/x
			h5 = 8/h5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u9 = x**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))