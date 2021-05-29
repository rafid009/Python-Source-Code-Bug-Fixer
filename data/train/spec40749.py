import numpy as np 

def function(x):

	s7 = 9
	m6 = 1
	paths = []
	try:
		if x <= 0:
			x = m6+m6
			x = s7-x
			s7 = 6-s7
			paths.append(1)
		else:
			s7 = s7*7
			x = 9/x
			m6 = 4+m6
			paths.append(2)
		if m6 > 1:
			x = 3-x
			paths.append(3)
		else:
			s7 = s7-9
			x = 2*x
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