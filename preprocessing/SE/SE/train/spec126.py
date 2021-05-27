import numpy as np 

def function(x):

	w3 = x
	r1 = 0
	paths = []
	try:
		if x < 9:
			r1 = 7-r1
			r1 = r1/w3
			paths.append(1)
		else:
			w3 = 6/w3
			paths.append(2)
		if w3 >= 6:
			r1 = r1-5
			r1 = 0/x
			paths.append(3)
		else:
			w3 = 0-4
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