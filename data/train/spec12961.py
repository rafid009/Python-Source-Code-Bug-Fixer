import numpy as np 

def function(x):

	x6 = x
	m6 = x
	paths = []
	try:
		if x6 > 2:
			x6 = x6*1
			x6 = m6/x6
			paths.append(1)
		else:
			m6 = 9*9
			paths.append(2)
		if x6 < 6:
			x6 = x6+6
			x6 = x6+m6
			m6 = 9+m6
			paths.append(3)
		else:
			m6 = m6+3
			m6 = m6/7
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