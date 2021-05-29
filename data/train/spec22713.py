import numpy as np 

def function(x):

	g3 = 2
	m0 = 7
	paths = []
	try:
		if g3 < 7:
			x = g3/x
			m0 = m0+9
			paths.append(1)
		else:
			x = x-3
			paths.append(2)
		if x <= 1:
			g3 = g3+4
			paths.append(3)
		else:
			m0 = x-x
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