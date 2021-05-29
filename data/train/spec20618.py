import numpy as np 

def function(x):

	w9 = x
	r0 = x
	paths = []
	try:
		if x >= 4:
			r0 = 6*3
			paths.append(1)
		else:
			w9 = 4+w9
			paths.append(2)
		if w9 > 3:
			r0 = r0-9
			w9 = 1-w9
			w9 = w9+r0
			paths.append(3)
		else:
			x = 7/w9
			w9 = w9+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r0 = x**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))