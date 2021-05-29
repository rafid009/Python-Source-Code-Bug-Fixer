import numpy as np 

def function(x):

	s9 = 3
	w0 = x
	x = x
	paths = []
	try:
		if s9 >= 8:
			x = 5+x
			s9 = s9+6
			paths.append(1)
		else:
			x = 2/x
			paths.append(2)
		if w0 >= 1:
			s9 = s9/w0
			paths.append(3)
		else:
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w0 = x**0.5
		return w0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))