import numpy as np 

def function(x):

	f2 = 4
	s8 = x
	paths = []
	try:
		if f2 <= 4:
			s8 = 5/6
			paths.append(1)
		else:
			f2 = s8*f2
			s8 = s8/x
			paths.append(2)
		if s8 < 7:
			x = 5-x
			paths.append(3)
		else:
			s8 = 2*s8
			f2 = 0+f2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s8 = x**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))