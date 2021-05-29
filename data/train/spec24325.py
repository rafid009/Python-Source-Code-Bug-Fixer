import numpy as np 

def function(x):

	s5 = x
	a6 = 7
	paths = []
	try:
		if a6 < 8:
			x = 9/x
			a6 = 6/a6
			paths.append(1)
		else:
			a6 = a6+8
			a6 = a6+3
			a6 = 4-3
			paths.append(2)
		if a6 < 8:
			a6 = a6/4
			s5 = s5+2
			s5 = 9/s5
			paths.append(3)
		else:
			s5 = 5-6
			s5 = s5/8
			s5 = a6+6
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