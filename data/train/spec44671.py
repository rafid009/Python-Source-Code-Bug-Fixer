import numpy as np 

def function(x):

	m9 = 8
	y9 = x
	paths = []
	try:
		if m9 <= 5:
			m9 = 1/3
			y9 = 2-4
			y9 = 2-y9
			paths.append(1)
		else:
			x = x/x
			x = m9/2
			paths.append(2)
		if x >= 9:
			x = x*8
			x = 5+x
			y9 = y9/4
			paths.append(3)
		else:
			x = 3*m9
			m9 = m9+8
			x = 3/y9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m9 = x**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))