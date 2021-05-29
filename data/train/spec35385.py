import numpy as np 

def function(x):

	h0 = x
	m8 = x
	paths = []
	try:
		if m8 < 6:
			m8 = m8/7
			paths.append(1)
		else:
			m8 = m8+1
			m8 = x/4
			x = x-6
			paths.append(2)
		if h0 > 4:
			x = h0/6
			m8 = 1-m8
			m8 = m8*x
			paths.append(3)
		else:
			x = x-m8
			x = m8*5
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