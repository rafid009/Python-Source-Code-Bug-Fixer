import numpy as np 

def function(x):

	s0 = 2
	q1 = x
	paths = []
	try:
		if q1 >= 0:
			q1 = q1*4
			paths.append(1)
		else:
			q1 = q1/2
			s0 = 1/1
			s0 = q1*9
			paths.append(2)
		if q1 >= 7:
			x = x/5
			paths.append(3)
		else:
			s0 = s0-0
			q1 = x/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q1 = x**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))