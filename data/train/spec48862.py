import numpy as np 

def function(x):

	s2 = x
	s8 = x
	x = 0
	paths = []
	try:
		if s2 >= 9:
			s2 = 1+x
			paths.append(1)
		else:
			x = 2/6
			x = s2*x
			s2 = 5+1
			paths.append(2)
		if s8 > 1:
			s2 = s2/8
			x = 8/6
			paths.append(3)
		else:
			s2 = 7*x
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