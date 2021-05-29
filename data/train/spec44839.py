import numpy as np 

def function(x):

	s0 = 0
	e7 = x
	paths = []
	try:
		if x < 0:
			s0 = s0/3
			paths.append(1)
		else:
			e7 = 7-s0
			x = 1+x
			paths.append(2)
		if s0 <= 3:
			x = 9*7
			s0 = s0-7
			s0 = s0-e7
			paths.append(3)
		else:
			s0 = 9-7
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		e7 = e7**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))