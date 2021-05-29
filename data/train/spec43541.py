import numpy as np 

def function(x):

	m0 = x
	q0 = x
	paths = []
	try:
		if q0 > 7:
			x = 8/x
			paths.append(1)
		else:
			x = 9-x
			q0 = m0+q0
			paths.append(2)
		if q0 > 2:
			m0 = m0+7
			m0 = x+q0
			paths.append(3)
		else:
			q0 = m0/q0
			x = 8-m0
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		x = m0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))