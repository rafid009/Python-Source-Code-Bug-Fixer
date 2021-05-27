import numpy as np 

def function(x):

	b5 = 7
	h5 = x
	paths = []
	try:
		if h5 < 5:
			h5 = 7*x
			paths.append(1)
		else:
			x = x+3
			paths.append(2)
		if x >= 8:
			x = x-h5
			x = 1+b5
			b5 = b5+9
			paths.append(3)
		else:
			h5 = h5+4
			b5 = b5/h5
			b5 = 3*b5
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