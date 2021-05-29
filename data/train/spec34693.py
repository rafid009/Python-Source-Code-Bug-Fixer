import numpy as np 

def function(x):

	s5 = x
	x = 6
	paths = []
	try:
		if s5 > 8:
			s5 = 7+4
			x = 2-5
			paths.append(1)
		else:
			x = s5/7
			paths.append(2)
		if s5 < 7:
			s5 = 2+4
			s5 = x-s5
			paths.append(3)
		else:
			s5 = 1*s5
			s5 = 4-x
			x = s5*s5
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		s5 = s5**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))