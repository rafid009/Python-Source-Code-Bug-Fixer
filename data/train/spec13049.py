import numpy as np 

def function(x):

	s5 = x
	z7 = x
	paths = []
	try:
		if s5 >= 3:
			x = s5*s5
			s5 = s5+8
			paths.append(1)
		else:
			x = 5-x
			s5 = s5+0
			s5 = 4/x
			paths.append(2)
		if x > 2:
			s5 = x*1
			s5 = s5*s5
			s5 = 2/8
			paths.append(3)
		else:
			z7 = x-7
			s5 = 0-z7
			z7 = 1*s5
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		s5 = z7**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))