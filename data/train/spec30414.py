import numpy as np 

def function(x):

	m1 = x
	m5 = 4
	paths = []
	try:
		if m5 <= 4:
			m1 = m1/x
			paths.append(1)
		else:
			m1 = m1-9
			paths.append(2)
		if m5 < 9:
			m1 = m1-9
			paths.append(3)
		else:
			x = 1-x
			m5 = m5*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m1 = x**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))