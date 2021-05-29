import numpy as np 

def function(x):

	s7 = x
	q2 = x
	paths = []
	try:
		if q2 >= 3:
			q2 = 5-5
			x = 9*7
			s7 = s7/s7
			paths.append(1)
		else:
			q2 = q2-1
			paths.append(2)
		if q2 < 4:
			q2 = q2/3
			paths.append(3)
		else:
			s7 = q2*6
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