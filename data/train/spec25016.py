import numpy as np 

def function(x):

	m0 = 8
	u0 = 2
	paths = []
	try:
		if x >= 0:
			m0 = 8-m0
			m0 = u0*m0
			x = u0-x
			paths.append(1)
		else:
			m0 = 9/m0
			x = u0-x
			paths.append(2)
		if m0 > 7:
			u0 = x-9
			paths.append(3)
		else:
			u0 = 0+u0
			u0 = u0+1
			x = 1-x
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