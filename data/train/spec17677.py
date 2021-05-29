import numpy as np 

def function(x):

	q4 = 8
	s2 = x
	paths = []
	try:
		if x >= 1:
			s2 = 6*3
			q4 = 2/x
			paths.append(1)
		else:
			s2 = s2+s2
			q4 = 6-3
			paths.append(2)
		if x > 2:
			x = 4/x
			paths.append(3)
		else:
			x = s2-x
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		s2 = s2**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))