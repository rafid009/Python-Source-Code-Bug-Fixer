import numpy as np 

def function(x):

	w9 = 2
	v1 = 1
	paths = []
	try:
		if x < 1:
			v1 = 9-v1
			v1 = x*v1
			paths.append(1)
		else:
			x = 0*x
			w9 = w9+1
			x = w9+x
			paths.append(2)
		if v1 < 8:
			w9 = 6*8
			w9 = w9*x
			paths.append(3)
		else:
			w9 = w9-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w9 = x**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))