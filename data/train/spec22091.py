import numpy as np 

def function(x):

	l2 = x
	s6 = 4
	paths = []
	try:
		if l2 >= 6:
			l2 = 5*x
			paths.append(1)
		else:
			l2 = 7+x
			s6 = x/2
			x = x*9
			paths.append(2)
		if s6 > 4:
			s6 = x/8
			l2 = l2+2
			s6 = x-s6
			paths.append(3)
		else:
			s6 = s6+0
			l2 = x*5
			s6 = l2+l2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s6 = x**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))