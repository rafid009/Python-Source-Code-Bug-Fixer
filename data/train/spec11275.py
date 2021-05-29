import numpy as np 

def function(x):

	h1 = 5
	w9 = x
	x = 8
	paths = []
	try:
		if w9 < 7:
			h1 = 3-x
			w9 = w9*9
			w9 = w9-6
			paths.append(1)
		else:
			w9 = h1-4
			w9 = 4/4
			w9 = w9+h1
			paths.append(2)
		if h1 > 4:
			w9 = 0+w9
			x = 8+h1
			w9 = w9-5
			paths.append(3)
		else:
			h1 = 1+h1
			x = 8+2
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		h1 = h1**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))