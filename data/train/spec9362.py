import numpy as np 

def function(x):

	w3 = 0
	h0 = 3
	paths = []
	try:
		if h0 < 2:
			w3 = h0/h0
			paths.append(1)
		else:
			w3 = 3+8
			w3 = 6-9
			paths.append(2)
		if h0 >= 5:
			w3 = w3+4
			paths.append(3)
		else:
			x = x+3
			x = x*8
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		h0 = w3**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))