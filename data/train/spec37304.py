import numpy as np 

def function(x):

	l8 = 4
	s5 = 8
	paths = []
	try:
		if l8 > 1:
			l8 = 0-l8
			s5 = l8*s5
			paths.append(1)
		else:
			s5 = 5/s5
			paths.append(2)
		if s5 > 9:
			l8 = l8+4
			s5 = s5/5
			paths.append(3)
		else:
			l8 = 6*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s5 = x**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))