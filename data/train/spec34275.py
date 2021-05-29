import numpy as np 

def function(x):

	s7 = x
	q2 = 4
	paths = []
	try:
		if x <= 5:
			s7 = s7-4
			paths.append(1)
		else:
			q2 = 7-q2
			q2 = q2*q2
			paths.append(2)
		if q2 > 6:
			x = 5-q2
			x = 3+1
			q2 = 7-8
			paths.append(3)
		else:
			x = x-0
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		s7 = s7**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))