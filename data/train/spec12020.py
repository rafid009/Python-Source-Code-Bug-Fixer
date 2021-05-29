import numpy as np 

def function(x):

	o5 = x
	s8 = 9
	paths = []
	try:
		if o5 > 7:
			o5 = 5*s8
			x = 3/x
			paths.append(1)
		else:
			s8 = 9*s8
			paths.append(2)
		if x < 2:
			x = x+6
			s8 = 9+s8
			paths.append(3)
		else:
			s8 = 0/s8
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