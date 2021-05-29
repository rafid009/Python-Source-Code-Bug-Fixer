import numpy as np 

def function(x):

	f0 = x
	h5 = 4
	paths = []
	try:
		if x < 0:
			h5 = h5+f0
			x = 6-x
			x = x-h5
			paths.append(1)
		else:
			f0 = f0/8
			paths.append(2)
		if f0 < 6:
			x = h5/7
			h5 = 7-h5
			paths.append(3)
		else:
			h5 = x*3
			x = 4*x
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		h5 = f0**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))