import numpy as np 

def function(x):

	m0 = x
	s6 = 7
	paths = []
	try:
		if m0 > 0:
			s6 = m0-3
			x = m0+x
			paths.append(1)
		else:
			x = 6*x
			x = x/m0
			x = 6/m0
			paths.append(2)
		if s6 <= 0:
			x = s6+m0
			m0 = m0+7
			x = 0-7
			paths.append(3)
		else:
			m0 = m0-4
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