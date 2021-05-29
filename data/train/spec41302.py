import numpy as np 

def function(x):

	h4 = x
	s9 = 7
	paths = []
	try:
		if x < 2:
			s9 = 4-s9
			paths.append(1)
		else:
			s9 = x*x
			x = x/h4
			paths.append(2)
		if x < 2:
			s9 = s9*x
			paths.append(3)
		else:
			x = x/x
			s9 = s9+5
			x = 5*x
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		s9 = h4**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))