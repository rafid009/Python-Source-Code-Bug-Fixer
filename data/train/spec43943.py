import numpy as np 

def function(x):

	a4 = x
	m8 = 3
	x = 1
	paths = []
	try:
		if x >= 8:
			x = a4*2
			a4 = 1*a4
			paths.append(1)
		else:
			m8 = m8*m8
			x = 6-x
			m8 = m8*m8
			paths.append(2)
		if x < 9:
			x = a4-9
			paths.append(3)
		else:
			a4 = 0/a4
			x = 7/x
			a4 = a4-x
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