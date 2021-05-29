import numpy as np 

def function(x):

	m7 = x
	s7 = 4
	paths = []
	try:
		if s7 <= 9:
			s7 = s7*m7
			s7 = 0-8
			paths.append(1)
		else:
			m7 = s7/3
			paths.append(2)
		if x < 0:
			x = x*x
			s7 = 3*s7
			paths.append(3)
		else:
			s7 = m7-9
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		s7 = s7**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))