import numpy as np 

def function(x):

	s7 = 4
	f5 = 4
	paths = []
	try:
		if s7 < 7:
			s7 = 0/3
			s7 = 8+s7
			f5 = f5-s7
			paths.append(1)
		else:
			f5 = 7+f5
			f5 = 6-f5
			s7 = s7+4
			paths.append(2)
		if x <= 7:
			s7 = 9-s7
			s7 = s7/x
			s7 = 5+3
			paths.append(3)
		else:
			s7 = 6/s7
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