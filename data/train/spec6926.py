import numpy as np 

def function(x):

	n2 = 7
	w4 = 8
	paths = []
	try:
		if n2 >= 1:
			w4 = 6*w4
			w4 = n2*w4
			paths.append(1)
		else:
			n2 = w4*n2
			paths.append(2)
		if x < 0:
			w4 = w4/2
			n2 = n2/n2
			w4 = w4*n2
			paths.append(3)
		else:
			x = 2/x
			x = x-w4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n2 = x**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))