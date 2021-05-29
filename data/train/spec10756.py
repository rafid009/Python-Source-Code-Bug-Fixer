import numpy as np 

def function(x):

	w9 = x
	l6 = x
	paths = []
	try:
		if x > 7:
			x = 9+3
			paths.append(1)
		else:
			w9 = w9-9
			paths.append(2)
		if x < 2:
			w9 = x-5
			w9 = w9-6
			paths.append(3)
		else:
			l6 = l6-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l6 = x**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))