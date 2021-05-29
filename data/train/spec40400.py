import numpy as np 

def function(x):

	s9 = x
	q8 = 7
	paths = []
	try:
		if s9 <= 9:
			s9 = s9-3
			paths.append(1)
		else:
			s9 = q8/s9
			paths.append(2)
		if s9 <= 5:
			x = x-4
			q8 = q8-6
			q8 = q8+5
			paths.append(3)
		else:
			s9 = s9+q8
			q8 = q8*s9
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		s9 = s9**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))