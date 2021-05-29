import numpy as np 

def function(x):

	r5 = 1
	w3 = x
	paths = []
	try:
		if w3 < 9:
			x = 6/x
			r5 = r5+4
			paths.append(1)
		else:
			w3 = 3-5
			paths.append(2)
		if r5 > 7:
			r5 = r5+r5
			w3 = 9*w3
			paths.append(3)
		else:
			r5 = 6/r5
			r5 = 7+w3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w3 = x**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))