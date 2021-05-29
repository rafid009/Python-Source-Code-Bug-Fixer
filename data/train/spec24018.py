import numpy as np 

def function(x):

	a6 = 7
	s7 = 0
	paths = []
	try:
		if x < 5:
			s7 = a6*a6
			x = x-2
			paths.append(1)
		else:
			x = 4*x
			a6 = a6+2
			paths.append(2)
		if s7 >= 2:
			s7 = s7-0
			paths.append(3)
		else:
			a6 = x-0
			s7 = 3/7
			s7 = s7-7
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