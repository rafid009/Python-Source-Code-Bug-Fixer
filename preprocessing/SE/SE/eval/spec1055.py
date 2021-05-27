import numpy as np 

def function(x):

	s7 = x
	j0 = x
	x = x
	paths = []
	try:
		if s7 >= 6:
			s7 = 6/s7
			s7 = 8-s7
			j0 = 6-j0
			paths.append(1)
		else:
			x = 7-2
			s7 = s7+6
			x = 9+6
			paths.append(2)
		if s7 > 7:
			j0 = j0+1
			s7 = s7+9
			paths.append(3)
		else:
			s7 = s7*9
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		s7 = j0**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))