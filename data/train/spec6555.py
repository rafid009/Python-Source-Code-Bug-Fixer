import numpy as np 

def function(x):

	s2 = 1
	m0 = 2
	paths = []
	try:
		if x < 4:
			m0 = s2/m0
			x = x+9
			paths.append(1)
		else:
			x = x+x
			x = x/x
			paths.append(2)
		if m0 > 4:
			m0 = 2-m0
			x = m0+2
			paths.append(3)
		else:
			s2 = x-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m0 = x**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))