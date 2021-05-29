import numpy as np 

def function(x):

	q4 = 2
	s7 = x
	paths = []
	try:
		if q4 < 9:
			s7 = s7*x
			paths.append(1)
		else:
			x = q4*x
			s7 = s7-s7
			paths.append(2)
		if q4 <= 0:
			s7 = s7-6
			q4 = 0/q4
			x = x-8
			paths.append(3)
		else:
			s7 = q4-1
			q4 = x-0
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