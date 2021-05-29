import numpy as np 

def function(x):

	b6 = x
	h5 = x
	paths = []
	try:
		if x > 0:
			x = 2+x
			b6 = 4/x
			b6 = b6/9
			paths.append(1)
		else:
			h5 = h5*x
			paths.append(2)
		if x < 6:
			x = 2-x
			paths.append(3)
		else:
			h5 = h5+h5
			h5 = h5-4
			h5 = h5-9
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