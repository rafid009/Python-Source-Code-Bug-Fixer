import numpy as np 

def function(x):

	h6 = x
	w6 = 4
	paths = []
	try:
		if h6 > 3:
			h6 = 4+0
			w6 = 5*w6
			paths.append(1)
		else:
			w6 = w6-h6
			h6 = 2-x
			paths.append(2)
		if w6 <= 7:
			w6 = 7/w6
			h6 = h6*6
			x = x-5
			paths.append(3)
		else:
			w6 = 3+w6
			w6 = h6-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h6 = x**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))