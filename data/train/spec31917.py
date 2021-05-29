import numpy as np 

def function(x):

	u1 = x
	m8 = 6
	paths = []
	try:
		if m8 < 0:
			x = x+9
			paths.append(1)
		else:
			m8 = m8*8
			u1 = u1+2
			paths.append(2)
		if m8 > 8:
			u1 = u1-m8
			u1 = 3-m8
			paths.append(3)
		else:
			m8 = m8/x
			m8 = m8/4
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