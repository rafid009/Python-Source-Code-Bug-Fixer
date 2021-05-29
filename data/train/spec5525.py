import numpy as np 

def function(x):

	f9 = 6
	s0 = x
	paths = []
	try:
		if f9 <= 6:
			f9 = 8*f9
			paths.append(1)
		else:
			x = x*s0
			f9 = 0*f9
			x = x-1
			paths.append(2)
		if x <= 3:
			s0 = 9*1
			s0 = 7*7
			s0 = s0+x
			paths.append(3)
		else:
			s0 = 6/x
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		s0 = s0**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))