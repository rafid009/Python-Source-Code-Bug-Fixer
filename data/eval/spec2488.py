import numpy as np 

def function(x):

	s7 = 2
	w3 = 6
	paths = []
	try:
		if x < 1:
			w3 = w3*w3
			w3 = w3+w3
			paths.append(1)
		else:
			w3 = w3-7
			paths.append(2)
		if x > 3:
			s7 = 9-s7
			paths.append(3)
		else:
			w3 = w3+3
			x = x*s7
			w3 = w3*w3
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