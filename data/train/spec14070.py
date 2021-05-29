import numpy as np 

def function(x):

	s6 = 0
	z1 = x
	paths = []
	try:
		if x > 6:
			s6 = 2+s6
			paths.append(1)
		else:
			z1 = 2+z1
			paths.append(2)
		if z1 >= 2:
			s6 = s6-z1
			z1 = 2/x
			paths.append(3)
		else:
			x = x*1
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		z1 = s6**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))