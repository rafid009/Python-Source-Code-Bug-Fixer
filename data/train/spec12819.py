import numpy as np 

def function(x):

	m4 = x
	u2 = x
	paths = []
	try:
		if x >= 4:
			m4 = m4/m4
			u2 = u2*9
			paths.append(1)
		else:
			u2 = u2*m4
			u2 = u2-x
			paths.append(2)
		if x >= 9:
			m4 = 4*m4
			u2 = u2+2
			paths.append(3)
		else:
			m4 = u2*5
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