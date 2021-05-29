import numpy as np 

def function(x):

	s2 = x
	q1 = x
	paths = []
	try:
		if q1 < 1:
			x = x/8
			paths.append(1)
		else:
			x = x+4
			x = x/5
			paths.append(2)
		if q1 >= 9:
			s2 = 2+x
			s2 = 0*9
			paths.append(3)
		else:
			s2 = 7-s2
			x = x-x
			x = 4*3
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		s2 = q1**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))