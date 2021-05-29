import numpy as np 

def function(x):

	f7 = 7
	h5 = 9
	paths = []
	try:
		if x <= 2:
			x = x*h5
			paths.append(1)
		else:
			h5 = h5*x
			paths.append(2)
		if x < 0:
			h5 = x/h5
			f7 = f7/3
			x = 6+x
			paths.append(3)
		else:
			x = h5*x
			f7 = 3*6
			h5 = f7+h5
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