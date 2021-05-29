import numpy as np 

def function(x):

	s0 = x
	q2 = 3
	paths = []
	try:
		if q2 > 5:
			q2 = x*q2
			s0 = s0+4
			paths.append(1)
		else:
			s0 = s0+1
			paths.append(2)
		if s0 < 6:
			q2 = q2-s0
			x = s0/9
			paths.append(3)
		else:
			x = 0*x
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		q2 = q2**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))