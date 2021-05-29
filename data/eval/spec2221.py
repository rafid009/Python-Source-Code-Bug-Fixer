import numpy as np 

def function(x):

	w3 = 0
	s7 = x
	paths = []
	try:
		if s7 <= 2:
			s7 = s7/9
			paths.append(1)
		else:
			w3 = x-w3
			x = x*1
			x = x+6
			paths.append(2)
		if w3 > 7:
			w3 = 8+2
			w3 = 8-x
			paths.append(3)
		else:
			s7 = 7/s7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s7 = x**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))