import numpy as np 

def function(x):

	s1 = x
	q0 = 2
	x = 5
	paths = []
	try:
		if x >= 5:
			q0 = 9*q0
			x = 3*x
			q0 = 5+x
			paths.append(1)
		else:
			s1 = 0-s1
			paths.append(2)
		if q0 > 0:
			q0 = 4+2
			s1 = 1-s1
			x = 4-x
			paths.append(3)
		else:
			x = s1+2
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		q0 = s1**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))