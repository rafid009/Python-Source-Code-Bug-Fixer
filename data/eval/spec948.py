import numpy as np 

def function(x):

	s4 = x
	w7 = 2
	paths = []
	try:
		if s4 < 0:
			w7 = 4-5
			w7 = 6/w7
			paths.append(1)
		else:
			s4 = s4+9
			s4 = s4+s4
			paths.append(2)
		if w7 <= 2:
			s4 = s4*s4
			paths.append(3)
		else:
			w7 = 1/w7
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