import numpy as np 

def function(x):

	q5 = x
	s8 = 2
	paths = []
	try:
		if x > 3:
			s8 = 2*s8
			x = 5/x
			q5 = 3*q5
			paths.append(1)
		else:
			s8 = s8-8
			paths.append(2)
		if s8 >= 2:
			q5 = s8-s8
			paths.append(3)
		else:
			x = q5/s8
			q5 = q5-2
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		q5 = q5**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))