import numpy as np 

def function(x):

	l6 = 2
	s6 = 8
	paths = []
	try:
		if l6 <= 9:
			s6 = s6*8
			s6 = x+9
			paths.append(1)
		else:
			l6 = 1*l6
			l6 = l6-3
			paths.append(2)
		if l6 > 3:
			x = 3+9
			s6 = 5+s6
			s6 = s6/7
			paths.append(3)
		else:
			s6 = 4-0
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