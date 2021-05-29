import numpy as np 

def function(x):

	z6 = 1
	s9 = x
	paths = []
	try:
		if s9 < 5:
			z6 = z6*6
			paths.append(1)
		else:
			x = 1/x
			paths.append(2)
		if x < 4:
			s9 = x-s9
			s9 = s9+4
			paths.append(3)
		else:
			z6 = 4-z6
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		x = s9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))