import numpy as np 

def function(x):

	y9 = 3
	m0 = x
	x = 9
	paths = []
	try:
		if y9 >= 1:
			m0 = m0/x
			y9 = 5/5
			paths.append(1)
		else:
			y9 = y9-y9
			paths.append(2)
		if m0 >= 3:
			y9 = y9/m0
			m0 = m0*9
			x = x+x
			paths.append(3)
		else:
			m0 = m0-9
			x = 8*5
			x = y9/2
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