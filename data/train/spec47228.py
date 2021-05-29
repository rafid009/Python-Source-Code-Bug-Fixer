import numpy as np 

def function(x):

	s7 = 9
	n9 = x
	paths = []
	try:
		if n9 > 6:
			s7 = s7/x
			paths.append(1)
		else:
			s7 = x+s7
			x = 5-x
			paths.append(2)
		if s7 >= 3:
			x = 4+x
			n9 = n9-2
			paths.append(3)
		else:
			s7 = 0-s7
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		s7 = s7**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))