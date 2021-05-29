import numpy as np 

def function(x):

	z9 = 7
	s4 = x
	paths = []
	try:
		if s4 < 6:
			s4 = s4-8
			paths.append(1)
		else:
			x = x/2
			z9 = s4-z9
			paths.append(2)
		if x <= 6:
			z9 = z9*9
			paths.append(3)
		else:
			s4 = s4*0
			z9 = 6*8
			x = 8+s4
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		z9 = s4**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))