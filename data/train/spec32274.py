import numpy as np 

def function(x):

	s8 = x
	z9 = 8
	x = x
	paths = []
	try:
		if z9 < 6:
			s8 = s8*8
			paths.append(1)
		else:
			x = 0*x
			x = x-4
			paths.append(2)
		if x <= 8:
			z9 = x-s8
			x = x/s8
			paths.append(3)
		else:
			x = x*4
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		z9 = s8**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))