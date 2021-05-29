import numpy as np 

def function(x):

	s2 = x
	m6 = 6
	paths = []
	try:
		if s2 < 7:
			s2 = 4-s2
			paths.append(1)
		else:
			x = 1/x
			x = x*1
			paths.append(2)
		if s2 >= 2:
			x = s2+3
			m6 = m6/4
			x = s2*2
			paths.append(3)
		else:
			m6 = 5-5
			m6 = m6+x
			s2 = 5/s2
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		m6 = s2**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))