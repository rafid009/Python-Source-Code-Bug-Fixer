import numpy as np 

def function(x):

	m5 = 7
	y9 = x
	x = x
	paths = []
	try:
		if m5 >= 0:
			x = 4/x
			m5 = m5+m5
			paths.append(1)
		else:
			y9 = m5*y9
			paths.append(2)
		if y9 < 8:
			m5 = m5*m5
			m5 = m5*2
			x = 1+m5
			paths.append(3)
		else:
			m5 = m5*6
			x = x/y9
			m5 = 3/m5
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		m5 = y9**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))