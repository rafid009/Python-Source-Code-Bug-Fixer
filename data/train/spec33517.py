import numpy as np 

def function(x):

	q2 = 6
	s9 = 8
	paths = []
	try:
		if x < 5:
			s9 = s9/4
			x = 8+x
			x = s9-x
			paths.append(1)
		else:
			q2 = 8*7
			s9 = s9*s9
			paths.append(2)
		if s9 > 9:
			s9 = x+8
			s9 = x-s9
			s9 = 7-s9
			paths.append(3)
		else:
			q2 = 7*q2
			q2 = 6*q2
			s9 = 1-q2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q2 = x**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))