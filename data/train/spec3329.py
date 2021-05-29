import numpy as np 

def function(x):

	n7 = 1
	w3 = 7
	paths = []
	try:
		if w3 >= 8:
			n7 = n7/2
			w3 = w3+w3
			x = w3-x
			paths.append(1)
		else:
			n7 = 9*n7
			n7 = w3*n7
			w3 = w3-x
			paths.append(2)
		if w3 >= 4:
			w3 = 3-w3
			w3 = w3/n7
			w3 = x/6
			paths.append(3)
		else:
			x = 5-x
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