import numpy as np 

def function(x):

	l2 = 1
	s6 = 0
	paths = []
	try:
		if l2 >= 2:
			l2 = 0+l2
			paths.append(1)
		else:
			l2 = l2*x
			paths.append(2)
		if s6 <= 5:
			s6 = s6-2
			paths.append(3)
		else:
			x = 0*x
			x = x*7
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