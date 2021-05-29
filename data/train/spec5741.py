import numpy as np 

def function(x):

	o1 = 5
	s8 = x
	paths = []
	try:
		if x <= 1:
			x = x*3
			o1 = o1/x
			paths.append(1)
		else:
			x = 0*3
			s8 = 0-s8
			x = x-x
			paths.append(2)
		if s8 < 2:
			s8 = s8*3
			x = x-6
			paths.append(3)
		else:
			s8 = 0*x
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		s8 = o1**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))