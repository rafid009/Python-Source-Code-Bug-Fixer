import numpy as np 

def function(x):

	m6 = x
	e9 = 8
	paths = []
	try:
		if m6 <= 4:
			x = 9*6
			m6 = 3-m6
			paths.append(1)
		else:
			x = 3-x
			m6 = m6+4
			paths.append(2)
		if x >= 3:
			x = 4+7
			x = 3-x
			paths.append(3)
		else:
			e9 = 1/x
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