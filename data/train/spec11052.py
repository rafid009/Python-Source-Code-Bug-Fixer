import numpy as np 

def function(x):

	s7 = x
	m0 = 9
	paths = []
	try:
		if m0 < 1:
			x = 7*x
			m0 = 1-m0
			m0 = m0+x
			paths.append(1)
		else:
			m0 = x-m0
			paths.append(2)
		if x <= 2:
			s7 = s7/7
			paths.append(3)
		else:
			m0 = m0-0
			s7 = s7*s7
			x = x-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))