import numpy as np 

def function(x):

	s0 = x
	q1 = x
	paths = []
	try:
		if q1 < 1:
			s0 = 3+s0
			s0 = q1/4
			s0 = s0+s0
			paths.append(1)
		else:
			s0 = s0+x
			s0 = 3-4
			q1 = 1-q1
			paths.append(2)
		if s0 > 4:
			s0 = 4*3
			x = 5-x
			s0 = 3+s0
			paths.append(3)
		else:
			x = 8/6
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		q1 = q1**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))