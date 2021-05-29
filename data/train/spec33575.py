import numpy as np 

def function(x):

	s8 = 4
	v5 = 4
	paths = []
	try:
		if v5 > 4:
			v5 = v5*x
			v5 = x+v5
			v5 = s8*3
			paths.append(1)
		else:
			v5 = v5*s8
			paths.append(2)
		if s8 > 8:
			x = 9/v5
			s8 = 2*s8
			paths.append(3)
		else:
			x = v5/x
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