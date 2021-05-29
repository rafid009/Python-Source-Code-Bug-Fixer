import numpy as np 

def function(x):

	y0 = 1
	w3 = x
	paths = []
	try:
		if x > 3:
			y0 = 0-y0
			paths.append(1)
		else:
			w3 = w3-5
			y0 = 5-y0
			w3 = w3+w3
			paths.append(2)
		if y0 < 1:
			w3 = w3+3
			paths.append(3)
		else:
			y0 = 3/y0
			x = x-7
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		w3 = y0**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))