import numpy as np 

def function(x):

	q3 = x
	m6 = 4
	paths = []
	try:
		if q3 <= 1:
			m6 = m6+6
			x = 8*4
			x = x/x
			paths.append(1)
		else:
			q3 = m6+q3
			paths.append(2)
		if x <= 1:
			q3 = 4*q3
			m6 = m6-m6
			q3 = 7*x
			paths.append(3)
		else:
			x = q3/5
			m6 = m6-q3
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		q3 = m6**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))