import numpy as np 

def function(x):

	q1 = 5
	m0 = x
	paths = []
	try:
		if q1 <= 2:
			q1 = 1/6
			q1 = q1-3
			paths.append(1)
		else:
			q1 = 0*m0
			q1 = 6-6
			q1 = 7*m0
			paths.append(2)
		if x > 8:
			q1 = 1/q1
			paths.append(3)
		else:
			q1 = q1*7
			x = 0/q1
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		m0 = m0**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))