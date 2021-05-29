import numpy as np 

def function(x):

	l7 = 3
	s0 = x
	paths = []
	try:
		if l7 >= 7:
			x = s0+x
			paths.append(1)
		else:
			s0 = s0*x
			s0 = s0/5
			l7 = s0/3
			paths.append(2)
		if l7 >= 9:
			x = x/9
			x = 2*x
			s0 = s0*9
			paths.append(3)
		else:
			s0 = 1/s0
			s0 = 1-s0
			x = x/7
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