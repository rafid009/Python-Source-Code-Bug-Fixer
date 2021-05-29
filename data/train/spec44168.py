import numpy as np 

def function(x):

	s0 = 2
	q9 = 3
	paths = []
	try:
		if q9 >= 0:
			q9 = s0/q9
			s0 = x*0
			paths.append(1)
		else:
			x = 0-2
			s0 = s0-5
			s0 = 2-x
			paths.append(2)
		if q9 > 7:
			q9 = q9-8
			s0 = s0-9
			paths.append(3)
		else:
			q9 = q9*s0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q9 = x**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))