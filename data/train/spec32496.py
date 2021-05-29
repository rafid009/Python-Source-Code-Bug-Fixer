import numpy as np 

def function(x):

	s4 = 2
	m4 = x
	paths = []
	try:
		if m4 > 0:
			m4 = s4-8
			paths.append(1)
		else:
			m4 = m4-8
			paths.append(2)
		if x < 1:
			m4 = x*2
			s4 = 1*s4
			paths.append(3)
		else:
			s4 = 9-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m4 = x**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))