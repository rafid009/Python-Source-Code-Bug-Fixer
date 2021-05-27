import numpy as np 

def function(x):

	s2 = x
	f2 = 2
	paths = []
	try:
		if x < 9:
			s2 = x-s2
			s2 = 3+s2
			paths.append(1)
		else:
			s2 = x-f2
			x = 5-x
			f2 = 8*5
			paths.append(2)
		if f2 > 6:
			x = 6-x
			s2 = 0/f2
			paths.append(3)
		else:
			f2 = x-f2
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