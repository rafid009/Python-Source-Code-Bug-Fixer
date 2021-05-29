import numpy as np 

def function(x):

	y8 = 9
	m6 = x
	paths = []
	try:
		if y8 <= 0:
			x = 2*x
			x = 4/x
			x = x-x
			paths.append(1)
		else:
			y8 = y8-x
			paths.append(2)
		if x <= 7:
			m6 = 4/m6
			y8 = y8/6
			paths.append(3)
		else:
			y8 = 9*y8
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