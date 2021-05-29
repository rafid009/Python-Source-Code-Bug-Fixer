import numpy as np 

def function(x):

	m8 = 4
	h5 = 7
	paths = []
	try:
		if h5 <= 8:
			x = x/6
			paths.append(1)
		else:
			x = x+7
			m8 = h5-x
			paths.append(2)
		if h5 > 3:
			x = m8-7
			h5 = x-h5
			paths.append(3)
		else:
			x = h5*7
			x = 6+h5
			m8 = 2*1
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		h5 = h5**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))