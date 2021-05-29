import numpy as np 

def function(x):

	w9 = x
	y8 = 1
	paths = []
	try:
		if w9 >= 8:
			y8 = y8*4
			y8 = y8*x
			paths.append(1)
		else:
			y8 = y8/2
			w9 = w9/y8
			x = y8-x
			paths.append(2)
		if x > 1:
			x = w9+0
			w9 = 0*5
			x = 6/y8
			paths.append(3)
		else:
			w9 = w9/1
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