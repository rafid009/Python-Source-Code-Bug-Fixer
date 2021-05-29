import numpy as np 

def function(x):

	s0 = 2
	m2 = x
	paths = []
	try:
		if x < 6:
			m2 = m2*x
			paths.append(1)
		else:
			m2 = m2-7
			paths.append(2)
		if m2 <= 2:
			x = x+7
			paths.append(3)
		else:
			s0 = 3+s0
			s0 = 2-s0
			s0 = m2+5
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