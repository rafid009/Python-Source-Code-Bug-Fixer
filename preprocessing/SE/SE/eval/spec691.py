import numpy as np 

def function(x):

	m3 = x
	m0 = x
	paths = []
	try:
		if m0 < 6:
			m0 = x/m0
			m0 = m0-7
			m3 = m3-4
			paths.append(1)
		else:
			m0 = 5-7
			paths.append(2)
		if x <= 3:
			x = 9+4
			paths.append(3)
		else:
			m0 = m3/m0
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