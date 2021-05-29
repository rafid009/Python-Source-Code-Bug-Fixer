import numpy as np 

def function(x):

	s2 = 7
	paths = []
	try:
		if s2 >= 9:
			s2 = 3*s2
			paths.append(1)
		else:
			s2 = s2/s2
			paths.append(2)
		if x >= 7:
			s2 = 4-5
			s2 = x/s2
			x = x/x
			paths.append(3)
		else:
			x = x*6
			x = x-8
			s2 = s2/3
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		s2 = s2**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))