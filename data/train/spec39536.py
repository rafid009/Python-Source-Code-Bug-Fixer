import numpy as np 

def function(x):

	e1 = x
	s0 = x
	paths = []
	try:
		if s0 > 0:
			x = x*2
			e1 = e1*x
			paths.append(1)
		else:
			e1 = 6*e1
			x = x*9
			e1 = 2-s0
			paths.append(2)
		if s0 < 5:
			x = x-e1
			e1 = e1-9
			x = s0/8
			paths.append(3)
		else:
			x = x-2
			s0 = 1/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s0 = x**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))