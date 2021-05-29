import numpy as np 

def function(x):

	q7 = x
	m0 = 3
	paths = []
	try:
		if m0 >= 0:
			m0 = m0-m0
			x = x+7
			paths.append(1)
		else:
			q7 = q7/q7
			m0 = 4-x
			m0 = 9-m0
			paths.append(2)
		if q7 < 7:
			q7 = q7-0
			x = m0/x
			paths.append(3)
		else:
			x = m0/5
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		x = q7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))