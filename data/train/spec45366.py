import numpy as np 

def function(x):

	s9 = 9
	m2 = x
	paths = []
	try:
		if s9 < 9:
			s9 = s9-3
			x = 2/1
			paths.append(1)
		else:
			s9 = s9-x
			paths.append(2)
		if x >= 5:
			x = s9-9
			s9 = s9*m2
			paths.append(3)
		else:
			s9 = x-s9
			m2 = 9*m2
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		m2 = m2**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))