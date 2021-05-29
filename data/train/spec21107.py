import numpy as np 

def function(x):

	z2 = 5
	s9 = x
	paths = []
	try:
		if z2 > 7:
			s9 = s9-5
			paths.append(1)
		else:
			z2 = x/z2
			s9 = 9/s9
			paths.append(2)
		if z2 < 0:
			z2 = 7/3
			paths.append(3)
		else:
			x = 8-x
			s9 = s9-s9
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		z2 = s9**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))