import numpy as np 

def function(x):

	w9 = x
	h1 = 7
	paths = []
	try:
		if h1 <= 2:
			h1 = w9+2
			paths.append(1)
		else:
			x = x/x
			x = x+w9
			paths.append(2)
		if h1 < 5:
			w9 = w9-3
			paths.append(3)
		else:
			h1 = h1*h1
			h1 = h1-6
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		h1 = w9**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))