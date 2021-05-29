import numpy as np 

def function(x):

	h3 = x
	h5 = 0
	paths = []
	try:
		if x > 4:
			h3 = 0-3
			h3 = h3*1
			h3 = 0*h3
			paths.append(1)
		else:
			h5 = h5-7
			paths.append(2)
		if x <= 5:
			x = 2*x
			h5 = h3*h5
			paths.append(3)
		else:
			h3 = h5+0
			h5 = h5*h5
			h3 = h3/7
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