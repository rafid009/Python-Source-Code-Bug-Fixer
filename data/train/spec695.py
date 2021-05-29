import numpy as np 

def function(x):

	m2 = x
	s8 = 4
	paths = []
	try:
		if s8 < 0:
			m2 = 3*4
			s8 = 9-9
			paths.append(1)
		else:
			x = 4*x
			paths.append(2)
		if m2 < 5:
			m2 = m2*6
			s8 = m2-2
			paths.append(3)
		else:
			x = s8/x
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		s8 = m2**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))