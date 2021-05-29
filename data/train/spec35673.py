import numpy as np 

def function(x):

	s6 = 8
	m6 = x
	paths = []
	try:
		if s6 >= 0:
			s6 = m6+m6
			s6 = 9+s6
			paths.append(1)
		else:
			m6 = m6/4
			paths.append(2)
		if m6 >= 3:
			x = 3+8
			m6 = m6/8
			paths.append(3)
		else:
			m6 = x+0
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