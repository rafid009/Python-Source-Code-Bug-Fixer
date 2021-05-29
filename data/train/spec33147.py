import numpy as np 

def function(x):

	m4 = x
	s6 = 0
	paths = []
	try:
		if m4 > 0:
			s6 = s6-x
			x = x-6
			paths.append(1)
		else:
			x = 9+0
			s6 = x*7
			paths.append(2)
		if m4 < 1:
			s6 = 9*x
			m4 = s6*6
			paths.append(3)
		else:
			m4 = x-4
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		s6 = m4**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))