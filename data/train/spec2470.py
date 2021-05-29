import numpy as np 

def function(x):

	l4 = x
	s2 = 4
	paths = []
	try:
		if s2 <= 1:
			x = x*s2
			s2 = x+8
			paths.append(1)
		else:
			l4 = l4-3
			paths.append(2)
		if s2 <= 7:
			s2 = s2*5
			paths.append(3)
		else:
			s2 = 5-s2
			s2 = l4-5
			s2 = 6+l4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l4 = x**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))