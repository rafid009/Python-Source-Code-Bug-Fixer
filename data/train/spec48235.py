import numpy as np 

def function(x):

	s0 = 3
	t5 = x
	paths = []
	try:
		if s0 < 8:
			x = 5+x
			paths.append(1)
		else:
			x = 2/x
			paths.append(2)
		if s0 > 4:
			x = s0/7
			s0 = t5+s0
			t5 = 4*6
			paths.append(3)
		else:
			s0 = s0+3
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