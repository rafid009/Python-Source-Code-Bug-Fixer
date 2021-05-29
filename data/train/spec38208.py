import numpy as np 

def function(x):

	o4 = 8
	w9 = x
	paths = []
	try:
		if o4 > 9:
			o4 = o4-6
			paths.append(1)
		else:
			x = 9-x
			paths.append(2)
		if o4 < 1:
			x = 1+2
			x = 6*4
			paths.append(3)
		else:
			w9 = w9*4
			o4 = o4+0
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