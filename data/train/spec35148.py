import numpy as np 

def function(x):

	u1 = 3
	m0 = 6
	paths = []
	try:
		if m0 > 0:
			m0 = m0+1
			x = x-u1
			u1 = 4-u1
			paths.append(1)
		else:
			u1 = u1-8
			m0 = x*m0
			paths.append(2)
		if m0 > 4:
			x = 3-4
			paths.append(3)
		else:
			u1 = 9*2
			m0 = m0*5
			m0 = m0-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))