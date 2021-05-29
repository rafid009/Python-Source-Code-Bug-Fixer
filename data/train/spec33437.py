import numpy as np 

def function(x):

	s7 = 8
	q2 = x
	paths = []
	try:
		if q2 <= 3:
			x = x-3
			q2 = x-s7
			paths.append(1)
		else:
			q2 = q2/q2
			s7 = s7-q2
			paths.append(2)
		if s7 <= 0:
			x = 9*x
			q2 = 6-q2
			q2 = 2*s7
			paths.append(3)
		else:
			s7 = s7+4
			q2 = q2-5
			x = x*s7
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		q2 = q2**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))