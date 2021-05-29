import numpy as np 

def function(x):

	z9 = 5
	s5 = x
	paths = []
	try:
		if z9 <= 5:
			z9 = 1-s5
			s5 = 9+s5
			s5 = 1-4
			paths.append(1)
		else:
			x = 6-s5
			paths.append(2)
		if z9 < 6:
			x = x*6
			s5 = s5+z9
			z9 = s5*z9
			paths.append(3)
		else:
			s5 = 1-s5
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		x = s5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))