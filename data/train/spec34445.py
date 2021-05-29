import numpy as np 

def function(x):

	m3 = x
	s0 = 9
	x = 4
	paths = []
	try:
		if m3 <= 5:
			m3 = m3/m3
			paths.append(1)
		else:
			m3 = 1*9
			m3 = 2*m3
			m3 = x+9
			paths.append(2)
		if s0 > 9:
			m3 = m3/2
			x = 6*s0
			paths.append(3)
		else:
			x = 2-m3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s0 = x**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))