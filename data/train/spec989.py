import numpy as np 

def function(x):

	n8 = 8
	w9 = x
	paths = []
	try:
		if x <= 8:
			w9 = 6/w9
			w9 = w9*4
			w9 = 1-w9
			paths.append(1)
		else:
			n8 = n8*7
			paths.append(2)
		if w9 >= 1:
			w9 = w9*n8
			paths.append(3)
		else:
			n8 = n8*x
			w9 = x-1
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