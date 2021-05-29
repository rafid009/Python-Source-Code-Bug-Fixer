import numpy as np 

def function(x):

	h2 = x
	w3 = 1
	paths = []
	try:
		if w3 < 6:
			w3 = 2+h2
			h2 = h2/3
			h2 = h2-3
			paths.append(1)
		else:
			h2 = h2-w3
			x = h2-x
			x = w3-x
			paths.append(2)
		if w3 < 2:
			w3 = 2+3
			h2 = h2/5
			h2 = w3*h2
			paths.append(3)
		else:
			h2 = 1-h2
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		h2 = h2**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))