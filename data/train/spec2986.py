import numpy as np 

def function(x):

	b2 = x
	h5 = 0
	paths = []
	try:
		if x < 5:
			x = x+x
			paths.append(1)
		else:
			b2 = 7*4
			b2 = h5*h5
			paths.append(2)
		if h5 < 0:
			x = x+7
			b2 = b2+7
			b2 = b2*3
			paths.append(3)
		else:
			h5 = h5-8
			h5 = 2*6
			x = x-4
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		h5 = b2**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))