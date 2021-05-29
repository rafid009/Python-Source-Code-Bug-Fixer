import numpy as np 

def function(x):

	s8 = x
	n9 = 2
	paths = []
	try:
		if n9 < 0:
			n9 = 4-9
			x = s8-x
			n9 = 9+n9
			paths.append(1)
		else:
			s8 = s8-9
			s8 = x+s8
			x = x/x
			paths.append(2)
		if n9 >= 5:
			n9 = 2/n9
			paths.append(3)
		else:
			x = n9-5
			s8 = x+s8
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