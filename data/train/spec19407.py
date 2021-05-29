import numpy as np 

def function(x):

	l7 = 5
	s2 = 5
	paths = []
	try:
		if s2 > 0:
			l7 = 9-l7
			l7 = 9*4
			paths.append(1)
		else:
			s2 = s2/7
			s2 = 6*6
			s2 = 8/1
			paths.append(2)
		if x <= 9:
			s2 = 4-8
			paths.append(3)
		else:
			s2 = 7*l7
			x = 5+2
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		l7 = s2**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))