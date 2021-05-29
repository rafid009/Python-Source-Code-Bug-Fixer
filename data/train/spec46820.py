import numpy as np 

def function(x):

	s7 = 3
	q9 = 2
	paths = []
	try:
		if q9 < 3:
			q9 = q9/q9
			x = x/7
			paths.append(1)
		else:
			x = 6-x
			s7 = s7*2
			s7 = 7-q9
			paths.append(2)
		if s7 <= 6:
			q9 = q9+9
			paths.append(3)
		else:
			q9 = 9*q9
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