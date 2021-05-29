import numpy as np 

def function(x):

	s0 = 1
	m9 = 8
	paths = []
	try:
		if x > 8:
			x = x-8
			paths.append(1)
		else:
			s0 = s0/s0
			x = 1-s0
			m9 = 3-8
			paths.append(2)
		if x >= 7:
			m9 = 7-4
			s0 = 1*1
			s0 = s0-7
			paths.append(3)
		else:
			x = s0-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m9 = x**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))