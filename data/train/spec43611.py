import numpy as np 

def function(x):

	m6 = 3
	q2 = 5
	paths = []
	try:
		if x < 8:
			m6 = m6/2
			q2 = 4-9
			q2 = q2*m6
			paths.append(1)
		else:
			q2 = x*q2
			paths.append(2)
		if x >= 9:
			m6 = q2*x
			paths.append(3)
		else:
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q2 = x**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))