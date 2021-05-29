import numpy as np 

def function(x):

	x5 = 2
	m6 = x
	paths = []
	try:
		if x5 <= 6:
			m6 = m6*6
			paths.append(1)
		else:
			x = 1-1
			x = 8/1
			paths.append(2)
		if m6 >= 8:
			x = x5/x
			paths.append(3)
		else:
			m6 = x-m6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x5 = x**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))