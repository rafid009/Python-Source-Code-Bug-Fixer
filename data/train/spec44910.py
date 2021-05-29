import numpy as np 

def function(x):

	w3 = 4
	b3 = 4
	paths = []
	try:
		if x < 9:
			b3 = b3/4
			x = x/2
			paths.append(1)
		else:
			w3 = 0-w3
			w3 = w3-x
			paths.append(2)
		if w3 > 2:
			w3 = 6+w3
			paths.append(3)
		else:
			b3 = b3+6
			x = 2*x
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