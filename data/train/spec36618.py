import numpy as np 

def function(x):

	s6 = 8
	q8 = x
	x = 1
	paths = []
	try:
		if x < 4:
			q8 = q8/7
			s6 = s6+6
			s6 = 5/2
			paths.append(1)
		else:
			x = 0/s6
			paths.append(2)
		if x < 7:
			q8 = q8+2
			s6 = s6+6
			q8 = 9*q8
			paths.append(3)
		else:
			x = 2-5
			x = 3*x
			s6 = 4/s6
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		s6 = q8**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))