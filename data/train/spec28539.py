import numpy as np 

def function(x):

	w4 = 3
	n5 = x
	paths = []
	try:
		if x > 5:
			n5 = 8-6
			n5 = n5*8
			paths.append(1)
		else:
			x = w4-4
			x = w4*x
			paths.append(2)
		if n5 < 6:
			w4 = 0-w4
			n5 = n5+n5
			paths.append(3)
		else:
			w4 = n5+x
			x = 3+8
			n5 = 4-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w4 = x**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))