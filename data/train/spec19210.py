import numpy as np 

def function(x):

	m6 = 8
	x = x
	paths = []
	try:
		if x >= 0:
			x = x+2
			m6 = m6-0
			paths.append(1)
		else:
			m6 = 9-m6
			paths.append(2)
		if x <= 5:
			m6 = m6-9
			paths.append(3)
		else:
			x = x-1
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