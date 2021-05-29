import numpy as np 

def function(x):

	s0 = 7
	m6 = 4
	paths = []
	try:
		if s0 >= 5:
			m6 = 6-m6
			s0 = s0/2
			m6 = 2-m6
			paths.append(1)
		else:
			s0 = m6-s0
			x = 5+x
			x = 1*x
			paths.append(2)
		if x > 2:
			x = s0*x
			m6 = m6/3
			paths.append(3)
		else:
			s0 = 5-s0
			m6 = m6+2
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