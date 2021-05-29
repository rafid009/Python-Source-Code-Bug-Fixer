import numpy as np 

def function(x):

	m0 = x
	q6 = x
	paths = []
	try:
		if q6 <= 9:
			m0 = 3-m0
			paths.append(1)
		else:
			m0 = 7-4
			x = m0-5
			paths.append(2)
		if m0 <= 7:
			q6 = 2/q6
			paths.append(3)
		else:
			q6 = 3-1
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		q6 = q6**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))