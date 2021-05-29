import numpy as np 

def function(x):

	s1 = x
	l6 = 5
	paths = []
	try:
		if s1 <= 3:
			x = x+4
			paths.append(1)
		else:
			l6 = l6-s1
			l6 = l6-2
			paths.append(2)
		if x <= 2:
			s1 = s1+s1
			l6 = 9/8
			paths.append(3)
		else:
			x = x-s1
			s1 = s1+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s1 = x**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))