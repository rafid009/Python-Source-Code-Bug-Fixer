import numpy as np 

def function(x):

	q2 = x
	m7 = 7
	paths = []
	try:
		if x > 0:
			m7 = 3*9
			x = q2*x
			paths.append(1)
		else:
			m7 = m7+2
			m7 = 6-m7
			paths.append(2)
		if q2 >= 9:
			q2 = 9*m7
			paths.append(3)
		else:
			q2 = q2*q2
			q2 = 6-q2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m7 = x**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))