import numpy as np 

def function(x):

	s2 = 7
	s5 = x
	paths = []
	try:
		if s5 <= 9:
			s5 = s5*4
			paths.append(1)
		else:
			s2 = 0-s2
			paths.append(2)
		if s5 > 6:
			s2 = s2-7
			x = 7-x
			x = s5*x
			paths.append(3)
		else:
			x = x*5
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