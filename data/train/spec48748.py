import numpy as np 

def function(x):

	s6 = x
	n9 = x
	x = x
	paths = []
	try:
		if s6 >= 3:
			s6 = n9/4
			n9 = x*n9
			paths.append(1)
		else:
			n9 = 0+n9
			n9 = n9-7
			paths.append(2)
		if s6 > 2:
			s6 = 4-8
			x = x+8
			paths.append(3)
		else:
			s6 = x/n9
			x = s6*s6
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		s6 = s6**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))