import numpy as np 

def function(x):

	h5 = x
	m0 = 6
	paths = []
	try:
		if h5 >= 2:
			m0 = 4*m0
			x = 8+x
			paths.append(1)
		else:
			m0 = 6+h5
			paths.append(2)
		if h5 > 8:
			h5 = m0*x
			h5 = 3-3
			paths.append(3)
		else:
			x = x*7
			x = 8*x
			m0 = m0/2
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		m0 = m0**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))