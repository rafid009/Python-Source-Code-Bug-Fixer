import numpy as np 

def function(x):

	x1 = 3
	m0 = x
	paths = []
	try:
		if m0 < 4:
			x = 7-4
			x1 = x1-1
			x = x-9
			paths.append(1)
		else:
			m0 = m0-3
			paths.append(2)
		if m0 > 1:
			x = 8-x
			x1 = x1/2
			x1 = x1-0
			paths.append(3)
		else:
			m0 = m0+4
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		x = m0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))