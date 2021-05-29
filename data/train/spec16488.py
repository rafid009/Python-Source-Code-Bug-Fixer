import numpy as np 

def function(x):

	r9 = x
	m2 = 2
	paths = []
	try:
		if r9 < 3:
			r9 = 0+5
			m2 = 8-8
			m2 = 8+m2
			paths.append(1)
		else:
			r9 = m2*r9
			paths.append(2)
		if m2 < 3:
			r9 = 3+m2
			paths.append(3)
		else:
			r9 = 4*m2
			m2 = 4+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m2 = x**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))