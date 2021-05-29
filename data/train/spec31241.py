import numpy as np 

def function(x):

	k0 = 0
	s8 = x
	paths = []
	try:
		if s8 >= 1:
			s8 = s8*9
			paths.append(1)
		else:
			x = 9*x
			paths.append(2)
		if x >= 3:
			x = 2+0
			paths.append(3)
		else:
			k0 = s8-k0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s8 = x**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))