import numpy as np 

def function(x):

	w8 = 8
	w7 = x
	paths = []
	try:
		if w7 > 5:
			w7 = w7/7
			paths.append(1)
		else:
			x = w7/6
			paths.append(2)
		if w8 < 0:
			w7 = 6-w7
			w8 = 5/w8
			x = w7/w8
			paths.append(3)
		else:
			w8 = w8-w8
			w8 = 3+w8
			w7 = 8-w7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w7 = x**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))