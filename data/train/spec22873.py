import numpy as np 

def function(x):

	m6 = x
	x7 = 2
	paths = []
	try:
		if x < 2:
			x = x/2
			paths.append(1)
		else:
			x7 = x7/6
			paths.append(2)
		if x7 >= 2:
			m6 = 8/7
			m6 = m6*2
			paths.append(3)
		else:
			m6 = x7-m6
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