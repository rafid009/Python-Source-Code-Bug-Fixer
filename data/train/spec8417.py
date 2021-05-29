import numpy as np 

def function(x):

	q6 = 6
	s0 = 6
	paths = []
	try:
		if x > 3:
			x = x-q6
			s0 = s0/4
			x = x/1
			paths.append(1)
		else:
			x = x-5
			x = 1-6
			x = 2+x
			paths.append(2)
		if x <= 1:
			s0 = s0-s0
			s0 = q6-0
			q6 = 2*q6
			paths.append(3)
		else:
			s0 = x-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q6 = x**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))