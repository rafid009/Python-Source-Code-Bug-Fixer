import numpy as np 

def function(x):

	x7 = x
	s1 = 3
	paths = []
	try:
		if x <= 4:
			x7 = 7-x7
			x = 3-8
			paths.append(1)
		else:
			x7 = s1+x
			s1 = s1-1
			x7 = x7+x7
			paths.append(2)
		if x7 <= 7:
			x = 3+x
			x7 = x+x7
			x7 = x-x7
			paths.append(3)
		else:
			x7 = 4+x7
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