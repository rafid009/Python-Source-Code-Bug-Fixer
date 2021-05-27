import numpy as np 

def function(x):

	m6 = x
	b9 = 3
	paths = []
	try:
		if x >= 7:
			m6 = 9-m6
			x = x*m6
			x = 1-x
			paths.append(1)
		else:
			x = x-x
			m6 = m6*8
			x = x-3
			paths.append(2)
		if b9 > 7:
			m6 = m6*6
			paths.append(3)
		else:
			m6 = 3-m6
			b9 = 2+4
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