import numpy as np 

def function(x):

	s7 = x
	z1 = 1
	paths = []
	try:
		if x > 5:
			s7 = 3+x
			x = 9+8
			paths.append(1)
		else:
			x = s7+5
			x = x*4
			paths.append(2)
		if x < 3:
			z1 = x/z1
			paths.append(3)
		else:
			z1 = z1+3
			z1 = z1-z1
			s7 = s7+0
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		z1 = z1**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))