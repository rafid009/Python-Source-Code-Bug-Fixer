import numpy as np 

def function(x):

	s8 = 6
	q2 = x
	paths = []
	try:
		if s8 > 3:
			x = x+x
			paths.append(1)
		else:
			s8 = s8/9
			x = x-8
			x = x/s8
			paths.append(2)
		if s8 > 9:
			x = x*x
			q2 = 2/q2
			x = s8*s8
			paths.append(3)
		else:
			q2 = 4*q2
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		s8 = q2**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))