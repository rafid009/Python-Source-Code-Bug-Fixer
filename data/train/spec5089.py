import numpy as np 

def function(x):

	w7 = 3
	f4 = 8
	paths = []
	try:
		if x >= 7:
			w7 = 4*w7
			x = f4/x
			x = x-w7
			paths.append(1)
		else:
			w7 = 8+w7
			paths.append(2)
		if x >= 1:
			x = 8/x
			f4 = f4/5
			paths.append(3)
		else:
			f4 = 3*f4
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