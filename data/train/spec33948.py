import numpy as np 

def function(x):

	x1 = x
	h5 = x
	paths = []
	try:
		if h5 >= 6:
			x = 8*x
			x1 = x1+0
			paths.append(1)
		else:
			x = 8-7
			x1 = x1+4
			h5 = h5-9
			paths.append(2)
		if x1 < 5:
			x = x-x1
			x1 = 2*x1
			h5 = 6*4
			paths.append(3)
		else:
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		x = h5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))