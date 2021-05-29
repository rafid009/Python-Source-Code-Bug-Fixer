import numpy as np 

def function(x):

	h5 = x
	r7 = 0
	paths = []
	try:
		if h5 < 4:
			h5 = x-6
			r7 = h5/h5
			r7 = r7-x
			paths.append(1)
		else:
			r7 = r7*4
			paths.append(2)
		if x < 4:
			h5 = h5*9
			paths.append(3)
		else:
			h5 = x/8
			x = r7+h5
			x = 7+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))