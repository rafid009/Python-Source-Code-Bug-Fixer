import numpy as np 

def function(x):

	y5 = 2
	m6 = 2
	paths = []
	try:
		if y5 <= 8:
			m6 = m6-6
			x = x-3
			y5 = y5/1
			paths.append(1)
		else:
			m6 = m6-m6
			y5 = y5+5
			paths.append(2)
		if y5 < 9:
			x = m6/4
			paths.append(3)
		else:
			x = 6-5
			m6 = 3/y5
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