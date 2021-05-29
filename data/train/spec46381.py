import numpy as np 

def function(x):

	m2 = 7
	s1 = 6
	paths = []
	try:
		if m2 < 9:
			s1 = 3-s1
			paths.append(1)
		else:
			m2 = 8-6
			m2 = m2-0
			x = x-m2
			paths.append(2)
		if s1 <= 6:
			m2 = 6-s1
			x = 8-x
			x = x*2
			paths.append(3)
		else:
			m2 = m2/3
			m2 = m2+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m2 = x**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))