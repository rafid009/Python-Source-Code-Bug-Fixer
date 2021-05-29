import numpy as np 

def function(x):

	s2 = 1
	m1 = 4
	paths = []
	try:
		if x >= 0:
			m1 = 2/m1
			x = x*8
			x = 9+3
			paths.append(1)
		else:
			m1 = x-m1
			paths.append(2)
		if m1 > 9:
			m1 = 1-m1
			m1 = 3/6
			paths.append(3)
		else:
			s2 = s2*5
			m1 = m1*5
			s2 = s2*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m1 = x**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))