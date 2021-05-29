import numpy as np 

def function(x):

	s8 = 1
	z6 = x
	paths = []
	try:
		if s8 <= 6:
			s8 = x+s8
			s8 = s8*0
			paths.append(1)
		else:
			z6 = z6*z6
			z6 = 2-x
			x = x*s8
			paths.append(2)
		if s8 > 0:
			z6 = z6/s8
			s8 = s8+1
			z6 = z6+6
			paths.append(3)
		else:
			x = 2*8
			x = 9+s8
			s8 = z6+4
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		z6 = s8**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))