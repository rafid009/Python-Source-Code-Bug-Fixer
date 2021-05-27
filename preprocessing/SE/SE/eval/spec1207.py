import numpy as np 

def function(x):

	h2 = x
	w5 = x
	paths = []
	try:
		if w5 >= 4:
			h2 = 2/w5
			paths.append(1)
		else:
			w5 = h2-w5
			h2 = h2-5
			paths.append(2)
		if h2 >= 8:
			h2 = w5*h2
			paths.append(3)
		else:
			x = 4-x
			h2 = h2-0
			h2 = h2+5
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