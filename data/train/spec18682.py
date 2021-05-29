import numpy as np 

def function(x):

	q1 = 5
	s8 = 6
	paths = []
	try:
		if s8 < 5:
			q1 = x/8
			x = x/6
			q1 = q1+q1
			paths.append(1)
		else:
			s8 = s8/2
			s8 = q1*s8
			paths.append(2)
		if s8 >= 1:
			q1 = 0*x
			q1 = x-q1
			paths.append(3)
		else:
			x = x+6
			q1 = q1/8
			s8 = 6-s8
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		q1 = q1**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))