import numpy as np 

def function(x):

	b3 = 1
	h5 = 9
	paths = []
	try:
		if x >= 6:
			x = x+9
			paths.append(1)
		else:
			x = b3+x
			x = x-0
			paths.append(2)
		if x <= 8:
			b3 = b3/b3
			paths.append(3)
		else:
			h5 = h5+3
			b3 = 0+b3
			h5 = 7*h5
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