import numpy as np 

def function(x):

	s9 = 8
	i7 = x
	paths = []
	try:
		if s9 < 0:
			s9 = 4-s9
			i7 = x-8
			paths.append(1)
		else:
			i7 = i7-s9
			x = 1/i7
			paths.append(2)
		if x <= 9:
			s9 = s9/5
			s9 = i7/7
			i7 = 3/i7
			paths.append(3)
		else:
			s9 = s9*7
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		s9 = i7**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))