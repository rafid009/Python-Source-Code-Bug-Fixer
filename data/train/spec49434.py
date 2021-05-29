import numpy as np 

def function(x):

	w3 = x
	n1 = 7
	paths = []
	try:
		if x > 3:
			x = x/4
			paths.append(1)
		else:
			n1 = 8*n1
			paths.append(2)
		if n1 > 0:
			n1 = x+n1
			paths.append(3)
		else:
			x = n1*3
			w3 = 6*w3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w3 = x**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))