import numpy as np 

def function(x):

	e1 = x
	s0 = 6
	paths = []
	try:
		if s0 < 4:
			x = 5-x
			paths.append(1)
		else:
			e1 = e1-1
			s0 = s0-s0
			s0 = s0*5
			paths.append(2)
		if e1 > 4:
			s0 = s0-3
			x = 7+e1
			e1 = s0/e1
			paths.append(3)
		else:
			s0 = s0+4
			s0 = s0-1
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		e1 = s0**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))