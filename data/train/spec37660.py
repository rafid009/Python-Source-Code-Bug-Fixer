import numpy as np 

def function(x):

	q2 = 4
	s5 = x
	paths = []
	try:
		if q2 <= 6:
			x = 2*s5
			q2 = q2-5
			x = q2*x
			paths.append(1)
		else:
			s5 = s5-s5
			x = 0*s5
			paths.append(2)
		if q2 >= 6:
			q2 = s5*x
			x = 5/3
			x = 9+6
			paths.append(3)
		else:
			s5 = s5+0
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