import numpy as np 

def function(x):

	n0 = x
	w7 = x
	paths = []
	try:
		if n0 <= 2:
			w7 = x-9
			n0 = 1*n0
			n0 = n0+5
			paths.append(1)
		else:
			x = 6*x
			x = x-9
			w7 = 5*w7
			paths.append(2)
		if n0 >= 0:
			x = n0+x
			paths.append(3)
		else:
			w7 = 5+w7
			w7 = w7-4
			x = w7/w7
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		n0 = w7**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))