import numpy as np 

def function(x):

	z8 = x
	s9 = 3
	paths = []
	try:
		if x <= 5:
			z8 = 5/z8
			s9 = x/s9
			paths.append(1)
		else:
			s9 = s9+9
			paths.append(2)
		if x < 6:
			x = x/x
			paths.append(3)
		else:
			s9 = s9-s9
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		z8 = s9**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))