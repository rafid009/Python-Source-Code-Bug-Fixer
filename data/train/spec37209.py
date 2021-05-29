import numpy as np 

def function(x):

	w8 = 8
	y9 = x
	paths = []
	try:
		if y9 <= 9:
			y9 = 1*y9
			w8 = 3+w8
			y9 = 8*y9
			paths.append(1)
		else:
			x = w8-9
			paths.append(2)
		if x >= 6:
			w8 = w8-w8
			x = 6/x
			w8 = 6*w8
			paths.append(3)
		else:
			x = x+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w8 = x**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))