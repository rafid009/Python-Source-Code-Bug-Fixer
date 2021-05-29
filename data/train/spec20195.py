import numpy as np 

def function(x):

	w4 = 3
	h2 = x
	paths = []
	try:
		if w4 < 7:
			w4 = w4-4
			w4 = w4*7
			paths.append(1)
		else:
			h2 = h2/x
			paths.append(2)
		if h2 >= 8:
			w4 = x+w4
			paths.append(3)
		else:
			x = x-x
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		x = w4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))