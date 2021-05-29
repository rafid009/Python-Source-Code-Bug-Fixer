import numpy as np 

def function(x):

	t8 = 1
	s7 = x
	paths = []
	try:
		if t8 > 8:
			s7 = 4-6
			paths.append(1)
		else:
			t8 = t8/1
			paths.append(2)
		if t8 > 2:
			s7 = 7/x
			t8 = t8+9
			paths.append(3)
		else:
			s7 = s7*t8
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