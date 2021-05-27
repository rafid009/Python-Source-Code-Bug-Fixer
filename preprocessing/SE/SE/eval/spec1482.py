import numpy as np 

def function(x):

	a9 = x
	m0 = 9
	paths = []
	try:
		if m0 < 3:
			m0 = m0+6
			x = a9+2
			paths.append(1)
		else:
			x = m0/x
			m0 = m0*m0
			a9 = 0-a9
			paths.append(2)
		if m0 < 7:
			a9 = m0*a9
			m0 = m0*2
			paths.append(3)
		else:
			m0 = m0*2
			x = x-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a9 = x**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))