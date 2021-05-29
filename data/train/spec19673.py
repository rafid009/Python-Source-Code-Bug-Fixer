import numpy as np 

def function(x):

	s6 = x
	w7 = x
	paths = []
	try:
		if s6 < 5:
			w7 = w7+4
			x = 7+x
			paths.append(1)
		else:
			s6 = s6-8
			x = 9/s6
			w7 = 5*3
			paths.append(2)
		if w7 >= 9:
			x = 1-s6
			x = w7/x
			x = x-0
			paths.append(3)
		else:
			x = 4/s6
			s6 = 3/s6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s6 = x**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))