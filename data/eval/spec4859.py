import numpy as np 

def function(x):

	s2 = 8
	n9 = 3
	paths = []
	try:
		if x <= 8:
			x = 2+n9
			paths.append(1)
		else:
			x = s2/x
			n9 = n9-s2
			paths.append(2)
		if n9 < 7:
			x = 5/8
			s2 = 5/8
			paths.append(3)
		else:
			s2 = s2-x
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		s2 = n9**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))