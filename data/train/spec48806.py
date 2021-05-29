import numpy as np 

def function(x):

	t0 = 2
	s7 = 3
	paths = []
	try:
		if s7 > 1:
			t0 = x/5
			paths.append(1)
		else:
			s7 = 0*t0
			s7 = s7-t0
			t0 = 2+t0
			paths.append(2)
		if s7 > 6:
			x = s7/x
			t0 = t0-x
			x = x/5
			paths.append(3)
		else:
			t0 = 9-t0
			t0 = s7-1
			t0 = 9-t0
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