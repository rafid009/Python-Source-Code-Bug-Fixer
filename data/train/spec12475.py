import numpy as np 

def function(x):

	z1 = x
	s9 = x
	paths = []
	try:
		if z1 <= 1:
			z1 = z1+x
			s9 = 0/1
			paths.append(1)
		else:
			z1 = z1+5
			x = 7*z1
			s9 = x/3
			paths.append(2)
		if x <= 0:
			s9 = s9+z1
			z1 = 3*1
			x = 9*8
			paths.append(3)
		else:
			z1 = 0-z1
			s9 = s9+4
			z1 = 6*z1
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		x = z1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))