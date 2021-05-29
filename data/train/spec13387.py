import numpy as np 

def function(x):

	s6 = 0
	z7 = 8
	paths = []
	try:
		if x < 3:
			s6 = s6*0
			x = z7+x
			paths.append(1)
		else:
			z7 = z7*z7
			x = s6/7
			paths.append(2)
		if s6 < 7:
			z7 = s6-z7
			x = 8+0
			x = 1-s6
			paths.append(3)
		else:
			x = 7+x
			x = z7-z7
			s6 = s6+3
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		s6 = z7**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))