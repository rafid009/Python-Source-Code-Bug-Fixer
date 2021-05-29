import numpy as np 

def function(x):

	k4 = x
	w3 = x
	paths = []
	try:
		if w3 < 9:
			k4 = 9/x
			paths.append(1)
		else:
			k4 = k4-6
			paths.append(2)
		if w3 >= 1:
			k4 = k4*6
			w3 = w3-7
			x = x*k4
			paths.append(3)
		else:
			k4 = k4-7
			k4 = k4-6
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