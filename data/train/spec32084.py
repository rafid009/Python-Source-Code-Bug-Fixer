import numpy as np 

def function(x):

	s6 = x
	m6 = x
	paths = []
	try:
		if x > 4:
			s6 = 9*s6
			s6 = 0+9
			s6 = s6+2
			paths.append(1)
		else:
			x = s6*7
			paths.append(2)
		if x > 4:
			x = x-8
			paths.append(3)
		else:
			x = 2*4
			m6 = m6*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s6 = x**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))