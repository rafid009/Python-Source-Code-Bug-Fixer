import numpy as np 

def function(x):

	s6 = 9
	e9 = x
	paths = []
	try:
		if s6 > 3:
			e9 = 3+e9
			e9 = 4-e9
			s6 = 8/s6
			paths.append(1)
		else:
			s6 = s6*s6
			paths.append(2)
		if s6 >= 0:
			e9 = e9+7
			paths.append(3)
		else:
			e9 = e9+e9
			x = x*e9
			s6 = s6*e9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e9 = x**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))