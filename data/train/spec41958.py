import numpy as np 

def function(x):

	q0 = x
	m6 = 9
	paths = []
	try:
		if x <= 8:
			x = x+5
			x = q0*7
			x = m6-x
			paths.append(1)
		else:
			m6 = m6*q0
			x = 6*x
			x = 8+3
			paths.append(2)
		if x > 2:
			x = 6-x
			x = 0+2
			paths.append(3)
		else:
			m6 = m6/x
			x = 2/7
			m6 = m6*7
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		q0 = m6**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))