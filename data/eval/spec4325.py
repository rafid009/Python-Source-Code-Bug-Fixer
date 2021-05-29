import numpy as np 

def function(x):

	s1 = 2
	q6 = 3
	paths = []
	try:
		if q6 <= 0:
			s1 = s1-5
			s1 = 3/q6
			q6 = q6/1
			paths.append(1)
		else:
			s1 = s1/7
			q6 = 0-q6
			s1 = 8-s1
			paths.append(2)
		if s1 >= 9:
			x = x*1
			s1 = s1/3
			paths.append(3)
		else:
			s1 = q6/s1
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		s1 = s1**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))