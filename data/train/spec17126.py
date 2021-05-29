import numpy as np 

def function(x):

	l7 = x
	w3 = x
	paths = []
	try:
		if l7 > 9:
			x = x-x
			l7 = l7-x
			paths.append(1)
		else:
			l7 = 9/l7
			w3 = 2*w3
			paths.append(2)
		if l7 < 9:
			w3 = l7-w3
			w3 = l7-4
			w3 = x/4
			paths.append(3)
		else:
			w3 = x*3
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