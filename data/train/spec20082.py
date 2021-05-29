import numpy as np 

def function(x):

	m6 = x
	s8 = x
	paths = []
	try:
		if x >= 1:
			s8 = s8/s8
			paths.append(1)
		else:
			m6 = m6*7
			paths.append(2)
		if x < 5:
			s8 = s8*5
			paths.append(3)
		else:
			s8 = x*m6
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