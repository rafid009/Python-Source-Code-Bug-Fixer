import numpy as np 

def function(x):

	m2 = x
	h5 = 8
	paths = []
	try:
		if x < 1:
			m2 = 5/7
			paths.append(1)
		else:
			h5 = 0/h5
			x = m2/x
			paths.append(2)
		if h5 >= 6:
			h5 = 8+7
			x = x-m2
			paths.append(3)
		else:
			m2 = m2-h5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m2 = x**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))