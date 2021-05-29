import numpy as np 

def function(x):

	m9 = x
	s4 = 0
	paths = []
	try:
		if m9 <= 9:
			m9 = m9*9
			s4 = m9-2
			paths.append(1)
		else:
			x = x+5
			paths.append(2)
		if s4 <= 6:
			m9 = m9-4
			paths.append(3)
		else:
			x = x+4
			x = 2/x
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