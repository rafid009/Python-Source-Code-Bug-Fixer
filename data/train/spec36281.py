import numpy as np 

def function(x):

	m9 = x
	s8 = 3
	paths = []
	try:
		if s8 > 2:
			x = 8*x
			m9 = m9/2
			paths.append(1)
		else:
			x = 5/x
			m9 = m9/2
			paths.append(2)
		if x > 8:
			x = x-6
			s8 = s8-5
			paths.append(3)
		else:
			m9 = 4*m9
			x = x/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s8 = x**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))