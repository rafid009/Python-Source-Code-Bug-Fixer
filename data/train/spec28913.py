import numpy as np 

def function(x):

	w9 = x
	z8 = 9
	paths = []
	try:
		if z8 >= 9:
			w9 = w9/7
			x = w9-x
			paths.append(1)
		else:
			w9 = w9/2
			w9 = w9+8
			x = 2-x
			paths.append(2)
		if x > 3:
			x = 1*3
			paths.append(3)
		else:
			x = w9-x
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