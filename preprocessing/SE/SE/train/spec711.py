import numpy as np 

def function(x):

	q7 = 6
	s2 = 5
	x = 2
	paths = []
	try:
		if s2 > 9:
			x = s2/s2
			paths.append(1)
		else:
			q7 = q7/5
			s2 = 4-s2
			s2 = s2+q7
			paths.append(2)
		if q7 > 6:
			x = x-q7
			paths.append(3)
		else:
			x = x*4
			x = 6*6
			q7 = 0-q7
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		q7 = q7**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))