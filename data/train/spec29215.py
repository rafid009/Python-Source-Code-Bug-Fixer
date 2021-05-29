import numpy as np 

def function(x):

	r5 = x
	h5 = x
	x = 3
	paths = []
	try:
		if h5 <= 6:
			x = r5+r5
			paths.append(1)
		else:
			x = x-6
			paths.append(2)
		if r5 <= 1:
			h5 = h5*8
			r5 = 3*r5
			r5 = r5-5
			paths.append(3)
		else:
			r5 = x+r5
			x = x-x
			r5 = h5+0
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