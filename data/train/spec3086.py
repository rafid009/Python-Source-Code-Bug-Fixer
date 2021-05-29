import numpy as np 

def function(x):

	m0 = 6
	h0 = 5
	paths = []
	try:
		if x >= 4:
			h0 = h0/5
			paths.append(1)
		else:
			h0 = h0/m0
			h0 = 0-h0
			paths.append(2)
		if h0 < 4:
			m0 = m0/8
			m0 = m0*h0
			paths.append(3)
		else:
			m0 = m0+6
			m0 = m0*5
			m0 = m0-0
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		m0 = h0**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))