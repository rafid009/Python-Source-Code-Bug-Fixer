import numpy as np 

def function(x):

	n3 = 5
	w5 = 2
	paths = []
	try:
		if n3 >= 9:
			x = x+n3
			x = 6*x
			paths.append(1)
		else:
			n3 = 9+n3
			paths.append(2)
		if w5 < 9:
			n3 = 4*n3
			w5 = 8+w5
			paths.append(3)
		else:
			x = w5*x
			n3 = 1*n3
			w5 = 2-w5
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