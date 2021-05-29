import numpy as np 

def function(x):

	s0 = 3
	m7 = x
	paths = []
	try:
		if m7 >= 3:
			m7 = 8+1
			x = 5*x
			m7 = m7-5
			paths.append(1)
		else:
			s0 = 6/s0
			x = x/6
			paths.append(2)
		if x > 8:
			m7 = 7-m7
			m7 = m7-s0
			s0 = m7-s0
			paths.append(3)
		else:
			s0 = s0/6
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		m7 = s0**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))