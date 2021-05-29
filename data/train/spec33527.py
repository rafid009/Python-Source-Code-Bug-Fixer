import numpy as np 

def function(x):

	g1 = x
	s8 = x
	paths = []
	try:
		if x > 4:
			x = x-1
			paths.append(1)
		else:
			s8 = x*s8
			s8 = s8-0
			paths.append(2)
		if x >= 8:
			s8 = 6/x
			paths.append(3)
		else:
			x = x+8
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