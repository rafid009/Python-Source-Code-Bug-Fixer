import numpy as np 

def function(x):

	s0 = 6
	m1 = 2
	paths = []
	try:
		if s0 > 3:
			m1 = 8-m1
			m1 = 7-m1
			paths.append(1)
		else:
			s0 = m1/s0
			x = m1-x
			paths.append(2)
		if s0 <= 0:
			m1 = 1/2
			s0 = 6-5
			paths.append(3)
		else:
			s0 = s0+m1
			s0 = 1+x
			x = x-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s0 = x**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))