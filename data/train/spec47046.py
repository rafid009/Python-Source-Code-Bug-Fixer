import numpy as np 

def function(x):

	n6 = 3
	w8 = x
	paths = []
	try:
		if w8 <= 7:
			x = x+0
			x = n6/9
			x = w8+0
			paths.append(1)
		else:
			n6 = w8/x
			w8 = 3-8
			paths.append(2)
		if x < 0:
			n6 = 1*n6
			paths.append(3)
		else:
			w8 = 6*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n6 = x**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))