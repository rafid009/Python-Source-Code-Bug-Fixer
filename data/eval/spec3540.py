import numpy as np 

def function(x):

	s4 = 5
	m4 = x
	paths = []
	try:
		if m4 > 9:
			m4 = x/m4
			paths.append(1)
		else:
			s4 = 0*s4
			paths.append(2)
		if s4 > 0:
			s4 = s4/9
			m4 = 0-m4
			s4 = x-m4
			paths.append(3)
		else:
			m4 = m4+m4
			m4 = 3-x
			x = 1-x
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