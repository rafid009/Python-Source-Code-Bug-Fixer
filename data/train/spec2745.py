import numpy as np 

def function(x):

	m0 = 0
	j1 = 9
	paths = []
	try:
		if m0 < 5:
			j1 = j1/j1
			x = m0*x
			paths.append(1)
		else:
			j1 = 1-9
			x = j1-1
			m0 = m0*9
			paths.append(2)
		if x > 8:
			x = x/x
			paths.append(3)
		else:
			x = x-3
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