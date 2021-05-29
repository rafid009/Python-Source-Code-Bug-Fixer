import numpy as np 

def function(x):

	e4 = x
	m4 = x
	paths = []
	try:
		if x <= 0:
			x = x*e4
			e4 = e4+8
			paths.append(1)
		else:
			m4 = 4-m4
			x = 1-4
			paths.append(2)
		if x < 8:
			m4 = 8+9
			paths.append(3)
		else:
			x = x+7
			m4 = m4+e4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e4 = x**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))