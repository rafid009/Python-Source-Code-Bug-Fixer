import numpy as np 

def function(x):

	h5 = x
	r7 = x
	paths = []
	try:
		if h5 > 1:
			r7 = r7*r7
			paths.append(1)
		else:
			x = 4*x
			r7 = h5+r7
			paths.append(2)
		if r7 <= 0:
			h5 = 0+h5
			x = h5+x
			paths.append(3)
		else:
			r7 = h5-5
			r7 = 5/r7
			h5 = h5-0
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