import numpy as np 

def function(x):

	q4 = x
	s6 = 7
	paths = []
	try:
		if q4 >= 2:
			q4 = q4+8
			paths.append(1)
		else:
			s6 = 9*4
			q4 = q4/1
			paths.append(2)
		if q4 < 5:
			s6 = 1*6
			paths.append(3)
		else:
			s6 = s6*1
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		s6 = q4**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))