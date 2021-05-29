import numpy as np 

def function(x):

	s0 = x
	q5 = 4
	paths = []
	try:
		if s0 >= 6:
			s0 = s0*7
			s0 = 0-s0
			s0 = s0*8
			paths.append(1)
		else:
			q5 = 9*8
			s0 = s0*8
			q5 = q5-9
			paths.append(2)
		if q5 <= 4:
			s0 = 3-s0
			paths.append(3)
		else:
			q5 = 4+0
			q5 = s0-q5
			s0 = x+0
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