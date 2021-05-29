import numpy as np 

def function(x):

	w3 = x
	h2 = 0
	x = x
	paths = []
	try:
		if w3 <= 5:
			h2 = h2*9
			h2 = w3+h2
			h2 = 7/3
			paths.append(1)
		else:
			w3 = h2-w3
			w3 = 1/w3
			paths.append(2)
		if x >= 7:
			x = x+w3
			paths.append(3)
		else:
			h2 = h2*h2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w3 = x**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))