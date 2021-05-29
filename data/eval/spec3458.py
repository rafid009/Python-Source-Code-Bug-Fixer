import numpy as np 

def function(x):

	j0 = x
	s8 = 8
	paths = []
	try:
		if s8 < 4:
			s8 = s8-j0
			paths.append(1)
		else:
			j0 = 2-x
			j0 = j0/2
			paths.append(2)
		if s8 >= 5:
			x = x+7
			j0 = 1*j0
			s8 = s8+s8
			paths.append(3)
		else:
			j0 = 0/8
			s8 = s8-4
			j0 = 0+j0
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		s8 = j0**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))