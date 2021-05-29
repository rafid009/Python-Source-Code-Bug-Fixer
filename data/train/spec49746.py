import numpy as np 

def function(x):

	s5 = 7
	a0 = x
	paths = []
	try:
		if s5 >= 5:
			s5 = s5-8
			x = 0-0
			a0 = 9-a0
			paths.append(1)
		else:
			a0 = a0/s5
			a0 = 5*6
			x = s5*x
			paths.append(2)
		if a0 < 8:
			a0 = 1-5
			paths.append(3)
		else:
			s5 = s5*s5
			x = x-9
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