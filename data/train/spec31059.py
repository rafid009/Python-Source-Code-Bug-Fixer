import numpy as np 

def function(x):

	e4 = x
	s1 = x
	x = x
	paths = []
	try:
		if e4 > 0:
			s1 = s1-1
			paths.append(1)
		else:
			x = 5-9
			paths.append(2)
		if x >= 0:
			s1 = 3+x
			e4 = 1/s1
			x = 2-6
			paths.append(3)
		else:
			s1 = s1*3
			x = 3-e4
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		s1 = s1**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))