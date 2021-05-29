import numpy as np 

def function(x):

	m2 = x
	s9 = x
	paths = []
	try:
		if x > 2:
			x = x+8
			paths.append(1)
		else:
			m2 = 1-3
			paths.append(2)
		if x > 0:
			s9 = s9*s9
			m2 = 0/x
			paths.append(3)
		else:
			m2 = x*7
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		m2 = s9**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))