import numpy as np 

def function(x):

	m0 = x
	f9 = x
	x = 6
	paths = []
	try:
		if x <= 0:
			x = 4-x
			f9 = 9+f9
			paths.append(1)
		else:
			f9 = m0-1
			paths.append(2)
		if m0 < 8:
			x = m0*x
			paths.append(3)
		else:
			x = 6/x
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