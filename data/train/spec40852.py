import numpy as np 

def function(x):

	h5 = x
	m4 = x
	paths = []
	try:
		if h5 <= 6:
			h5 = h5-6
			x = h5-x
			paths.append(1)
		else:
			x = h5/x
			m4 = m4-7
			paths.append(2)
		if x > 5:
			m4 = m4*m4
			paths.append(3)
		else:
			x = 6-0
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		h5 = m4**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))