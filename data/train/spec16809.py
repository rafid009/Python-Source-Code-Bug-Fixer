import numpy as np 

def function(x):

	x3 = 7
	s1 = x
	paths = []
	try:
		if x3 < 8:
			x3 = x3*x
			paths.append(1)
		else:
			x3 = 8-x3
			s1 = 7-s1
			paths.append(2)
		if x3 < 6:
			x = x+1
			paths.append(3)
		else:
			s1 = 8+9
			x3 = s1*s1
			x3 = s1/3
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		s1 = x3**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))