import numpy as np 

def function(x):

	s4 = x
	m2 = x
	x = 5
	paths = []
	try:
		if s4 <= 1:
			m2 = s4/2
			paths.append(1)
		else:
			s4 = 4/6
			paths.append(2)
		if m2 <= 9:
			m2 = m2-4
			m2 = m2+3
			paths.append(3)
		else:
			x = x-8
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		s4 = s4**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))