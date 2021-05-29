import numpy as np 

def function(x):

	s2 = 8
	w6 = 0
	paths = []
	try:
		if s2 > 1:
			x = x-9
			paths.append(1)
		else:
			x = 0-0
			paths.append(2)
		if w6 > 5:
			w6 = w6*w6
			s2 = s2*x
			s2 = s2*w6
			paths.append(3)
		else:
			w6 = x-3
			x = 1-s2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s2 = x**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))