import numpy as np 

def function(x):

	e0 = x
	m4 = 6
	paths = []
	try:
		if e0 <= 5:
			m4 = m4*9
			paths.append(1)
		else:
			e0 = m4-m4
			paths.append(2)
		if m4 >= 1:
			m4 = e0-m4
			m4 = x+m4
			paths.append(3)
		else:
			e0 = e0-9
			m4 = 4+0
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