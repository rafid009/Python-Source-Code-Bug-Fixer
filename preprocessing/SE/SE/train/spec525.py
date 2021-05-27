import numpy as np 

def function(x):

	s1 = 2
	a7 = x
	paths = []
	try:
		if s1 >= 7:
			a7 = 4*5
			paths.append(1)
		else:
			s1 = s1/3
			paths.append(2)
		if s1 > 9:
			a7 = 1+5
			s1 = 4/a7
			paths.append(3)
		else:
			a7 = a7+7
			s1 = 4-s1
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