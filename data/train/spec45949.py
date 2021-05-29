import numpy as np 

def function(x):

	w7 = x
	h1 = x
	paths = []
	try:
		if h1 >= 4:
			w7 = w7/h1
			paths.append(1)
		else:
			h1 = 9*5
			w7 = 8+w7
			h1 = 5/h1
			paths.append(2)
		if w7 >= 9:
			w7 = w7*h1
			paths.append(3)
		else:
			w7 = h1/w7
			w7 = w7+2
			h1 = h1-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h1 = x**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))