import numpy as np 

def function(x):

	b2 = 7
	h5 = x
	paths = []
	try:
		if h5 <= 1:
			x = x*1
			paths.append(1)
		else:
			h5 = h5/1
			b2 = 0+8
			h5 = b2-5
			paths.append(2)
		if x >= 8:
			x = h5/4
			paths.append(3)
		else:
			b2 = 5-h5
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