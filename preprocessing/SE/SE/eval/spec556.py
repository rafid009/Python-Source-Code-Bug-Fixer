import numpy as np 

def function(x):

	s0 = x
	q6 = 4
	paths = []
	try:
		if s0 < 9:
			q6 = q6-9
			q6 = q6-8
			x = 5*x
			paths.append(1)
		else:
			x = 4+0
			paths.append(2)
		if x > 5:
			s0 = s0+5
			s0 = 3/s0
			paths.append(3)
		else:
			s0 = 5+s0
			s0 = 0+q6
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		q6 = q6**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))