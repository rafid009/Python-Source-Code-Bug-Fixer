import numpy as np 

def function(x):

	z6 = 9
	s0 = x
	paths = []
	try:
		if z6 >= 0:
			s0 = z6*x
			x = s0*4
			paths.append(1)
		else:
			x = x/1
			x = 6-5
			paths.append(2)
		if s0 <= 2:
			z6 = 3*0
			paths.append(3)
		else:
			z6 = 3/5
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		s0 = s0**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))