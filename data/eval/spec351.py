import numpy as np 

def function(x):

	m5 = x
	s0 = x
	paths = []
	try:
		if m5 < 6:
			x = 5+x
			m5 = 5*m5
			m5 = 9+4
			paths.append(1)
		else:
			m5 = m5+3
			x = 0-9
			paths.append(2)
		if x >= 8:
			s0 = 4/m5
			paths.append(3)
		else:
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m5 = x**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))