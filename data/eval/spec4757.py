import numpy as np 

def function(x):

	x5 = 8
	m0 = 3
	paths = []
	try:
		if m0 >= 5:
			x = x-6
			m0 = x/2
			paths.append(1)
		else:
			m0 = m0-x5
			x = m0*x
			paths.append(2)
		if x < 1:
			x5 = 4*4
			paths.append(3)
		else:
			x5 = x5*8
			m0 = 1/1
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