import numpy as np 

def function(x):

	m8 = 2
	e2 = 9
	paths = []
	try:
		if x < 3:
			x = 5*m8
			x = 4-6
			e2 = m8*4
			paths.append(1)
		else:
			x = x-x
			x = e2+e2
			paths.append(2)
		if x < 7:
			x = x-e2
			paths.append(3)
		else:
			m8 = x/x
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