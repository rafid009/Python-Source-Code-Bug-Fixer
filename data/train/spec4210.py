import numpy as np 

def function(x):

	z9 = x
	s8 = 2
	paths = []
	try:
		if s8 >= 0:
			z9 = z9*7
			x = 3*x
			z9 = 2*x
			paths.append(1)
		else:
			x = x*0
			x = s8+6
			z9 = z9*1
			paths.append(2)
		if s8 < 3:
			x = x*6
			s8 = s8+2
			paths.append(3)
		else:
			z9 = s8+4
			z9 = z9/7
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		s8 = z9**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))