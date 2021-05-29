import numpy as np 

def function(x):

	i9 = x
	w4 = x
	paths = []
	try:
		if w4 <= 3:
			w4 = 8/w4
			w4 = 6*w4
			paths.append(1)
		else:
			w4 = i9+5
			i9 = i9*9
			x = x/w4
			paths.append(2)
		if w4 <= 3:
			x = w4-4
			i9 = i9-0
			paths.append(3)
		else:
			w4 = 3+w4
			w4 = x-2
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