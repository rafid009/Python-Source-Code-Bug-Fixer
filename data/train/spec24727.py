import numpy as np 

def function(x):

	s8 = 6
	q0 = 6
	paths = []
	try:
		if q0 > 3:
			s8 = 3/6
			paths.append(1)
		else:
			s8 = 5*x
			paths.append(2)
		if x <= 1:
			x = 1-x
			x = x-s8
			paths.append(3)
		else:
			s8 = s8-7
			q0 = 8/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q0 = x**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))