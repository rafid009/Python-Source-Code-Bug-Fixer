import numpy as np 

def function(x):

	m2 = x
	m0 = x
	paths = []
	try:
		if m2 <= 2:
			m0 = x+5
			m2 = x-7
			m0 = m0*7
			paths.append(1)
		else:
			m0 = 0+m0
			paths.append(2)
		if m0 <= 6:
			m0 = m0-x
			m2 = m0-x
			paths.append(3)
		else:
			m0 = 8-8
			m2 = m0/2
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		x = m2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))