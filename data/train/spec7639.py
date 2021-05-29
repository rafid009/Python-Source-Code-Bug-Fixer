import numpy as np 

def function(x):

	q1 = 5
	m6 = x
	paths = []
	try:
		if q1 < 5:
			m6 = 8-8
			m6 = 9-m6
			x = 5/x
			paths.append(1)
		else:
			m6 = m6*x
			q1 = q1+0
			paths.append(2)
		if x >= 9:
			x = 7*5
			q1 = 5-q1
			q1 = 6+q1
			paths.append(3)
		else:
			m6 = m6/1
			q1 = m6+4
			x = x-m6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m6 = x**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))