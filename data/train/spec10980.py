import numpy as np 

def function(x):

	w7 = x
	s2 = 3
	paths = []
	try:
		if x >= 9:
			w7 = w7*w7
			paths.append(1)
		else:
			w7 = x*x
			s2 = 2*s2
			paths.append(2)
		if w7 >= 9:
			s2 = s2-s2
			w7 = 1-8
			paths.append(3)
		else:
			w7 = 2*w7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w7 = x**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))