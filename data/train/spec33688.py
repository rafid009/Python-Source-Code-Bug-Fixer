import numpy as np 

def function(x):

	n1 = x
	s2 = x
	paths = []
	try:
		if s2 >= 1:
			n1 = s2/9
			paths.append(1)
		else:
			n1 = 4-n1
			paths.append(2)
		if s2 <= 1:
			x = 6*x
			paths.append(3)
		else:
			s2 = 8-s2
			s2 = 1+1
			n1 = n1/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s2 = x**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))