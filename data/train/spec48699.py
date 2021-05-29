import numpy as np 

def function(x):

	h5 = 1
	h3 = 4
	paths = []
	try:
		if x < 8:
			h3 = h3/5
			h3 = 8-h3
			h3 = h3*7
			paths.append(1)
		else:
			x = 5/h5
			h3 = h3-4
			paths.append(2)
		if h3 > 9:
			h3 = 6+h3
			h5 = x/h5
			h3 = 0*2
			paths.append(3)
		else:
			h3 = 7/4
			h3 = h3-9
			h3 = h3*8
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