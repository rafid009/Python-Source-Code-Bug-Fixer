import numpy as np 

def function(x):

	s0 = 6
	q6 = 2
	paths = []
	try:
		if s0 > 6:
			x = x-1
			s0 = 0+4
			x = 7+x
			paths.append(1)
		else:
			s0 = s0/x
			x = 9-1
			x = x/9
			paths.append(2)
		if s0 > 5:
			q6 = q6/5
			s0 = s0/s0
			paths.append(3)
		else:
			s0 = s0-7
			x = x-x
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		q6 = s0**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))