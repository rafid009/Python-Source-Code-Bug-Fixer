import numpy as np 

def function(x):

	w9 = x
	y1 = x
	x = 1
	paths = []
	try:
		if y1 < 0:
			w9 = 6*1
			y1 = y1-3
			paths.append(1)
		else:
			w9 = w9*w9
			paths.append(2)
		if w9 < 8:
			w9 = w9+9
			w9 = 5+w9
			x = w9-x
			paths.append(3)
		else:
			x = 2-7
			x = w9/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w9 = x**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))