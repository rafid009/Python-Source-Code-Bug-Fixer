import numpy as np 

def function(x):

	z2 = 8
	s5 = x
	paths = []
	try:
		if s5 < 7:
			s5 = 3-9
			x = x/9
			s5 = s5+z2
			paths.append(1)
		else:
			s5 = x/z2
			paths.append(2)
		if z2 > 5:
			z2 = z2-s5
			paths.append(3)
		else:
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))