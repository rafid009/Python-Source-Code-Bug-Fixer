import numpy as np 

def function(x):

	b8 = x
	h5 = 5
	paths = []
	try:
		if x < 3:
			h5 = h5+h5
			paths.append(1)
		else:
			h5 = h5+2
			x = x/x
			paths.append(2)
		if h5 < 5:
			h5 = b8/3
			paths.append(3)
		else:
			b8 = 5-h5
			x = 1/4
			h5 = h5-7
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		x = b8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))