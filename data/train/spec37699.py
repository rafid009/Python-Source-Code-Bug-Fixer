import numpy as np 

def function(x):

	b8 = x
	h5 = x
	paths = []
	try:
		if h5 > 4:
			b8 = b8*x
			x = 5*8
			paths.append(1)
		else:
			x = 1+b8
			paths.append(2)
		if h5 >= 2:
			b8 = b8*h5
			x = 7/x
			paths.append(3)
		else:
			b8 = b8/7
			h5 = h5+0
			h5 = h5-h5
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