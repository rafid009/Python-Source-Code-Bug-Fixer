import numpy as np 

def function(x):

	z0 = 1
	w7 = 9
	paths = []
	try:
		if x < 4:
			x = 9*x
			paths.append(1)
		else:
			w7 = w7*w7
			paths.append(2)
		if w7 < 7:
			w7 = w7*w7
			paths.append(3)
		else:
			w7 = w7/3
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