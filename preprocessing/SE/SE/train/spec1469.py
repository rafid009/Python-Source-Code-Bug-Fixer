import numpy as np 

def function(x):

	i1 = 6
	s8 = x
	paths = []
	try:
		if i1 < 8:
			i1 = i1+9
			paths.append(1)
		else:
			x = s8*x
			s8 = i1/x
			paths.append(2)
		if i1 < 9:
			i1 = 3*9
			x = x-8
			paths.append(3)
		else:
			s8 = 0-s8
			s8 = s8+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))