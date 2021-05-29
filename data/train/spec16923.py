import numpy as np 

def function(x):

	r4 = 1
	h5 = 2
	paths = []
	try:
		if h5 > 1:
			r4 = x-r4
			paths.append(1)
		else:
			x = 2+x
			r4 = 4*r4
			paths.append(2)
		if h5 < 0:
			x = x-9
			h5 = 6/x
			paths.append(3)
		else:
			h5 = 3-h5
			r4 = 1+r4
			r4 = 6/x
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		r4 = r4**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))