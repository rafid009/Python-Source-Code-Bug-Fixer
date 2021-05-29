import numpy as np 

def function(x):

	n7 = x
	w2 = x
	paths = []
	try:
		if w2 < 9:
			w2 = 8/w2
			n7 = 1-n7
			paths.append(1)
		else:
			x = 3-x
			paths.append(2)
		if x >= 2:
			n7 = 4*n7
			paths.append(3)
		else:
			n7 = n7-w2
			n7 = 9-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n7 = x**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))