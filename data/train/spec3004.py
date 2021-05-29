import numpy as np 

def function(x):

	b0 = x
	h5 = 8
	paths = []
	try:
		if h5 > 4:
			h5 = 5/3
			h5 = h5*4
			paths.append(1)
		else:
			h5 = h5-h5
			h5 = h5/1
			paths.append(2)
		if x > 6:
			b0 = b0+9
			paths.append(3)
		else:
			b0 = 6-9
			b0 = b0-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b0 = x**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))