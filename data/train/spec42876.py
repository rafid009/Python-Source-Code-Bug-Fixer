import numpy as np 

def function(x):

	a9 = 6
	w9 = x
	paths = []
	try:
		if x < 6:
			w9 = 0+8
			paths.append(1)
		else:
			a9 = 6-a9
			a9 = 0-w9
			paths.append(2)
		if w9 <= 6:
			a9 = 7-x
			w9 = w9+6
			a9 = a9*w9
			paths.append(3)
		else:
			w9 = x+6
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