import numpy as np 

def function(x):

	s6 = x
	m4 = x
	paths = []
	try:
		if x < 0:
			m4 = m4-3
			paths.append(1)
		else:
			s6 = 4*s6
			paths.append(2)
		if x > 3:
			m4 = 5-m4
			s6 = s6+2
			paths.append(3)
		else:
			m4 = m4/s6
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		s6 = s6**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))