import numpy as np 

def function(x):

	w4 = 0
	n5 = x
	paths = []
	try:
		if x < 4:
			n5 = w4*1
			paths.append(1)
		else:
			w4 = 7+x
			n5 = n5+2
			x = w4*7
			paths.append(2)
		if w4 < 8:
			w4 = 8-w4
			paths.append(3)
		else:
			n5 = n5*n5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n5 = x**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))