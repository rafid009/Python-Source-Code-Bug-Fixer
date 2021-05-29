import numpy as np 

def function(x):

	b9 = x
	m4 = 0
	x = 9
	paths = []
	try:
		if x <= 9:
			m4 = m4/2
			m4 = 9-m4
			paths.append(1)
		else:
			m4 = m4*3
			b9 = b9-0
			paths.append(2)
		if m4 >= 2:
			b9 = m4-3
			x = 8-x
			m4 = m4/1
			paths.append(3)
		else:
			x = 0-8
			m4 = m4-m4
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