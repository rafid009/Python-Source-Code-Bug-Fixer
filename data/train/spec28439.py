import numpy as np 

def function(x):

	m0 = 2
	j1 = x
	paths = []
	try:
		if x <= 4:
			m0 = 0*j1
			paths.append(1)
		else:
			x = 9/1
			m0 = m0*m0
			x = 4*m0
			paths.append(2)
		if j1 <= 6:
			j1 = j1-1
			paths.append(3)
		else:
			m0 = 3/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m0 = x**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))