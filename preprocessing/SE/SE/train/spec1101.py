import numpy as np 

def function(x):

	s7 = 9
	e7 = 2
	paths = []
	try:
		if s7 > 1:
			x = 9*x
			x = x-9
			paths.append(1)
		else:
			x = x-6
			x = 7-9
			s7 = 5*4
			paths.append(2)
		if x <= 5:
			e7 = e7*x
			s7 = s7+x
			paths.append(3)
		else:
			e7 = 1/6
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		s7 = s7**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))