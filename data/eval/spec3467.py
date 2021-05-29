import numpy as np 

def function(x):

	x9 = 9
	s4 = x
	x = 8
	paths = []
	try:
		if s4 > 4:
			s4 = 3+s4
			x9 = x9-3
			x = 5/x
			paths.append(1)
		else:
			x = x+4
			paths.append(2)
		if x > 4:
			x = 7-x
			paths.append(3)
		else:
			x9 = s4+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s4 = x**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))