import numpy as np 

def function(x):

	m0 = x
	h5 = x
	paths = []
	try:
		if h5 <= 7:
			x = h5-m0
			m0 = 7+2
			x = x/4
			paths.append(1)
		else:
			h5 = x/h5
			paths.append(2)
		if x >= 6:
			m0 = m0*3
			x = 3-4
			paths.append(3)
		else:
			m0 = h5+h5
			x = 1/7
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