import numpy as np 

def function(x):

	w9 = 4
	q6 = x
	paths = []
	try:
		if w9 <= 0:
			q6 = q6-q6
			w9 = 4/q6
			paths.append(1)
		else:
			w9 = w9+6
			paths.append(2)
		if w9 >= 8:
			q6 = 2*q6
			paths.append(3)
		else:
			w9 = w9-7
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		w9 = q6**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))