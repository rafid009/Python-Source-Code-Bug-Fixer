import numpy as np 

def function(x):

	m6 = x
	y0 = x
	paths = []
	try:
		if m6 <= 9:
			m6 = m6+1
			paths.append(1)
		else:
			m6 = 6-m6
			m6 = m6*m6
			x = x-8
			paths.append(2)
		if x < 6:
			x = 7*y0
			paths.append(3)
		else:
			m6 = 6*4
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		m6 = y0**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))