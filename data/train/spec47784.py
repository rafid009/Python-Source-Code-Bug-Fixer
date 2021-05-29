import numpy as np 

def function(x):

	s1 = x
	x1 = 1
	paths = []
	try:
		if x <= 9:
			x = x+0
			paths.append(1)
		else:
			x = 1-5
			paths.append(2)
		if s1 <= 5:
			x1 = 8/x1
			x = x-s1
			x1 = 7/5
			paths.append(3)
		else:
			s1 = x-s1
			s1 = 4+x1
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