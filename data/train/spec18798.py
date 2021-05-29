import numpy as np 

def function(x):

	h5 = x
	e4 = x
	paths = []
	try:
		if e4 >= 1:
			x = 0*3
			x = 8*h5
			h5 = h5-h5
			paths.append(1)
		else:
			h5 = h5/5
			paths.append(2)
		if e4 > 0:
			x = 8-x
			e4 = h5+4
			paths.append(3)
		else:
			e4 = e4+3
			e4 = e4+4
			x = x/5
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