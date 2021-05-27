import numpy as np 

def function(x):

	h6 = 3
	m8 = 5
	paths = []
	try:
		if h6 < 6:
			h6 = 6+h6
			m8 = 6-2
			paths.append(1)
		else:
			m8 = 7*m8
			m8 = 0*4
			paths.append(2)
		if h6 >= 1:
			h6 = 2+h6
			m8 = x/m8
			paths.append(3)
		else:
			m8 = x/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m8 = x**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))