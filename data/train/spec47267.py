import numpy as np 

def function(x):

	r5 = 4
	h5 = x
	paths = []
	try:
		if x <= 1:
			r5 = r5/r5
			h5 = 8-h5
			paths.append(1)
		else:
			h5 = r5-h5
			r5 = r5+3
			paths.append(2)
		if h5 < 1:
			r5 = x-r5
			paths.append(3)
		else:
			r5 = x*r5
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		r5 = r5**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))