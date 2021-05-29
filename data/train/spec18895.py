import numpy as np 

def function(x):

	m6 = x
	x7 = 8
	paths = []
	try:
		if x7 <= 8:
			x = x-5
			x7 = 5/x7
			paths.append(1)
		else:
			x7 = 4-9
			paths.append(2)
		if x7 > 8:
			x = x/2
			m6 = 1/2
			x = x+x7
			paths.append(3)
		else:
			x = x+0
			x = m6*x
			x7 = 9-x7
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