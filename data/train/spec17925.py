import numpy as np 

def function(x):

	w4 = x
	h2 = 5
	paths = []
	try:
		if w4 < 9:
			h2 = h2+w4
			w4 = w4/3
			paths.append(1)
		else:
			h2 = 5-x
			h2 = 5/w4
			w4 = w4/w4
			paths.append(2)
		if x < 0:
			x = x-4
			h2 = x-7
			x = 6/x
			paths.append(3)
		else:
			x = 8+6
			w4 = w4/w4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h2 = x**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))