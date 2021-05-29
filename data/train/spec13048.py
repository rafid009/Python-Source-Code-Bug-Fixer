import numpy as np 

def function(x):

	e0 = 7
	m6 = 3
	paths = []
	try:
		if e0 > 6:
			m6 = 5-m6
			m6 = m6*m6
			paths.append(1)
		else:
			x = 0-x
			paths.append(2)
		if m6 < 3:
			e0 = e0-2
			paths.append(3)
		else:
			m6 = 8-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e0 = x**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))