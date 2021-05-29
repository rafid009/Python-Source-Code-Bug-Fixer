import numpy as np 

def function(x):

	s2 = 7
	d2 = x
	paths = []
	try:
		if x <= 7:
			s2 = x-6
			paths.append(1)
		else:
			d2 = 6*x
			paths.append(2)
		if s2 > 9:
			s2 = d2+4
			s2 = 2-5
			s2 = 7-s2
			paths.append(3)
		else:
			s2 = 8+s2
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