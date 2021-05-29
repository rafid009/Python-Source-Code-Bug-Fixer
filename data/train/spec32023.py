import numpy as np 

def function(x):

	s2 = x
	t0 = 2
	paths = []
	try:
		if s2 <= 8:
			x = x-1
			paths.append(1)
		else:
			x = 8/x
			paths.append(2)
		if t0 <= 2:
			x = x-1
			paths.append(3)
		else:
			t0 = 0+2
			t0 = t0/8
			s2 = s2-x
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