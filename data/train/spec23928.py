import numpy as np 

def function(x):

	l9 = 7
	s6 = x
	paths = []
	try:
		if x <= 9:
			x = 4/8
			s6 = s6-0
			s6 = 1/s6
			paths.append(1)
		else:
			l9 = 7+8
			s6 = s6+0
			l9 = 1+3
			paths.append(2)
		if l9 < 4:
			l9 = 8+8
			s6 = s6-3
			paths.append(3)
		else:
			x = x-l9
			s6 = 6+4
			s6 = 5/9
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