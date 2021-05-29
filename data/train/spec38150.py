import numpy as np 

def function(x):

	i4 = 9
	s8 = 4
	paths = []
	try:
		if s8 > 9:
			x = 5+5
			paths.append(1)
		else:
			i4 = 0+i4
			paths.append(2)
		if i4 < 9:
			s8 = s8+7
			i4 = 3-x
			paths.append(3)
		else:
			s8 = 9/2
			i4 = s8/4
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