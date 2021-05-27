import numpy as np 

def function(x):

	m6 = 8
	q0 = 5
	paths = []
	try:
		if q0 < 2:
			q0 = q0/m6
			paths.append(1)
		else:
			x = 3-x
			q0 = q0*q0
			paths.append(2)
		if m6 < 9:
			m6 = m6*2
			m6 = x-m6
			paths.append(3)
		else:
			x = 2+2
			m6 = 0-q0
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		m6 = m6**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))