import numpy as np 

def function(x):

	u3 = 3
	m4 = 0
	paths = []
	try:
		if m4 <= 8:
			u3 = u3-m4
			m4 = 1-4
			u3 = u3-m4
			paths.append(1)
		else:
			x = 1*m4
			u3 = u3*4
			paths.append(2)
		if m4 <= 3:
			x = x*u3
			m4 = 0-8
			u3 = 4*u3
			paths.append(3)
		else:
			x = 5-3
			m4 = 6/m4
			u3 = m4+u3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m4 = x**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))