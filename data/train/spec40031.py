import numpy as np 

def function(x):

	s1 = 3
	n9 = 6
	paths = []
	try:
		if s1 >= 3:
			n9 = n9-9
			paths.append(1)
		else:
			s1 = 1*s1
			s1 = 4/n9
			n9 = 9/4
			paths.append(2)
		if x <= 7:
			n9 = n9+9
			n9 = 3*n9
			x = x/6
			paths.append(3)
		else:
			n9 = n9*n9
			n9 = x+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s1 = x**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))