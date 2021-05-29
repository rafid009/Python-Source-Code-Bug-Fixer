import numpy as np 

def function(x):

	s2 = x
	s8 = 0
	paths = []
	try:
		if s8 >= 8:
			x = x/x
			x = x/7
			paths.append(1)
		else:
			s8 = s8+4
			s8 = s8/7
			s2 = 9*s2
			paths.append(2)
		if s8 >= 6:
			s8 = x+s8
			paths.append(3)
		else:
			s2 = s2*s8
			x = 7*2
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