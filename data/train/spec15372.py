import numpy as np 

def function(x):

	m6 = 8
	r7 = 4
	paths = []
	try:
		if m6 >= 6:
			r7 = 9-3
			x = x-7
			m6 = 6/6
			paths.append(1)
		else:
			m6 = m6-x
			m6 = r7/m6
			paths.append(2)
		if m6 >= 2:
			m6 = 4-m6
			r7 = 2+r7
			paths.append(3)
		else:
			m6 = m6*4
			r7 = r7+4
			m6 = m6+m6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m6 = x**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))