import numpy as np 

def function(x):

	s6 = x
	t9 = x
	paths = []
	try:
		if s6 <= 1:
			x = x+x
			x = t9+x
			t9 = x-t9
			paths.append(1)
		else:
			t9 = 2-t9
			t9 = 4-t9
			paths.append(2)
		if x < 0:
			t9 = 3+t9
			paths.append(3)
		else:
			t9 = t9+x
			x = x-x
			s6 = 3*s6
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