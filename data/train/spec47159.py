import numpy as np 

def function(x):

	a9 = x
	m6 = 7
	paths = []
	try:
		if x > 9:
			m6 = 6+m6
			m6 = m6+8
			a9 = m6+m6
			paths.append(1)
		else:
			m6 = m6-9
			a9 = 2/a9
			a9 = a9-6
			paths.append(2)
		if x < 4:
			a9 = 7*9
			paths.append(3)
		else:
			x = x-m6
			a9 = x-2
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