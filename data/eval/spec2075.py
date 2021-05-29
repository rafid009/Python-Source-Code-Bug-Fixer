import numpy as np 

def function(x):

	m6 = 1
	h5 = 4
	paths = []
	try:
		if x > 1:
			m6 = m6/9
			x = m6/x
			x = x*x
			paths.append(1)
		else:
			x = x+8
			h5 = 5+h5
			paths.append(2)
		if x >= 8:
			h5 = x-x
			m6 = m6+m6
			paths.append(3)
		else:
			x = 0+x
			x = x-x
			x = 1-9
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