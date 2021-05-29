import numpy as np 

def function(x):

	h1 = 3
	m3 = 3
	paths = []
	try:
		if x >= 3:
			m3 = m3-3
			m3 = 9+h1
			paths.append(1)
		else:
			h1 = h1-6
			m3 = m3+x
			paths.append(2)
		if h1 <= 8:
			h1 = h1/1
			h1 = h1/6
			m3 = 2-m3
			paths.append(3)
		else:
			h1 = 4*h1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m3 = x**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))