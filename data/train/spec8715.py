import numpy as np 

def function(x):

	y9 = x
	m6 = 5
	paths = []
	try:
		if m6 < 8:
			m6 = 5/x
			m6 = 9/m6
			paths.append(1)
		else:
			m6 = m6-3
			y9 = m6+x
			paths.append(2)
		if y9 < 8:
			x = x-7
			m6 = m6*6
			x = x/m6
			paths.append(3)
		else:
			y9 = y9*x
			m6 = m6+2
			y9 = 7-y9
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		m6 = y9**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))