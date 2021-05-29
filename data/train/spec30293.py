import numpy as np 

def function(x):

	a8 = x
	m0 = 4
	paths = []
	try:
		if m0 > 0:
			x = 4*4
			x = x-0
			paths.append(1)
		else:
			a8 = 7-a8
			paths.append(2)
		if m0 < 3:
			m0 = 9+2
			paths.append(3)
		else:
			m0 = x+a8
			m0 = 8+m0
			x = x-m0
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