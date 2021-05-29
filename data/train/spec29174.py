import numpy as np 

def function(x):

	u0 = 5
	m6 = 7
	paths = []
	try:
		if x > 2:
			m6 = u0*m6
			m6 = x-m6
			x = m6-x
			paths.append(1)
		else:
			m6 = 8*8
			u0 = u0/2
			u0 = 2/7
			paths.append(2)
		if m6 > 8:
			u0 = u0*u0
			m6 = x*u0
			paths.append(3)
		else:
			m6 = m6-x
			x = u0/x
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		m6 = m6**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))