import numpy as np 

def function(x):

	r0 = 0
	h5 = x
	paths = []
	try:
		if x <= 2:
			x = x*1
			paths.append(1)
		else:
			x = h5/x
			x = x-x
			paths.append(2)
		if h5 > 3:
			h5 = h5+h5
			paths.append(3)
		else:
			h5 = h5*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r0 = x**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))