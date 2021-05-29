import numpy as np 

def function(x):

	s1 = 3
	z1 = x
	x = x
	paths = []
	try:
		if s1 < 9:
			x = 6-s1
			paths.append(1)
		else:
			z1 = z1*7
			paths.append(2)
		if s1 > 6:
			z1 = 5*6
			z1 = 9/z1
			z1 = 8/s1
			paths.append(3)
		else:
			x = x+x
			x = x/8
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		s1 = z1**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))