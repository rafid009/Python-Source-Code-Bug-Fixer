import numpy as np 

def function(x):

	d9 = 7
	m0 = 7
	paths = []
	try:
		if m0 <= 7:
			m0 = m0+3
			paths.append(1)
		else:
			x = 5*3
			m0 = m0*m0
			d9 = m0*d9
			paths.append(2)
		if x <= 0:
			m0 = 7*8
			paths.append(3)
		else:
			m0 = m0-m0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m0 = x**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))