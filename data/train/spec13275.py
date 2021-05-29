import numpy as np 

def function(x):

	m6 = 0
	e6 = 9
	paths = []
	try:
		if e6 >= 3:
			m6 = m6-2
			e6 = e6-8
			paths.append(1)
		else:
			m6 = 4*m6
			e6 = 6*9
			paths.append(2)
		if m6 >= 3:
			m6 = 0*e6
			paths.append(3)
		else:
			m6 = 4*1
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