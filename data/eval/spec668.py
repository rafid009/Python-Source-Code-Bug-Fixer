import numpy as np 

def function(x):

	w8 = x
	w9 = 3
	paths = []
	try:
		if w8 > 7:
			w8 = w8-x
			paths.append(1)
		else:
			w9 = 6/5
			w9 = 9*w9
			paths.append(2)
		if x < 8:
			w9 = w9*w8
			w9 = x-3
			paths.append(3)
		else:
			x = 1/x
			w9 = w9+0
			x = 8+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))