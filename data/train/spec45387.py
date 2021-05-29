import numpy as np 

def function(x):

	l2 = 2
	s6 = 0
	x = x
	paths = []
	try:
		if l2 < 0:
			x = x-l2
			x = 7/x
			s6 = 0/s6
			paths.append(1)
		else:
			l2 = l2-7
			x = x/8
			paths.append(2)
		if s6 > 8:
			x = x/s6
			s6 = 0*l2
			l2 = 5*3
			paths.append(3)
		else:
			x = x+6
			l2 = l2*6
			x = 4/x
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		s6 = l2**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))