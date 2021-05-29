import numpy as np 

def function(x):

	s6 = 9
	e5 = x
	paths = []
	try:
		if x <= 8:
			e5 = 1/e5
			paths.append(1)
		else:
			s6 = s6*7
			x = 4*x
			e5 = s6*1
			paths.append(2)
		if s6 >= 2:
			x = e5*x
			x = e5-5
			s6 = s6*7
			paths.append(3)
		else:
			x = s6*x
			e5 = e5/e5
			e5 = x/e5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s6 = x**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))