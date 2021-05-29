import numpy as np 

def function(x):

	m3 = 4
	h5 = 4
	paths = []
	try:
		if m3 <= 2:
			h5 = h5-h5
			m3 = m3/7
			paths.append(1)
		else:
			h5 = h5+5
			m3 = m3+3
			paths.append(2)
		if x < 8:
			m3 = x*m3
			x = 8-x
			paths.append(3)
		else:
			h5 = 4*h5
			m3 = x-9
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		h5 = m3**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))