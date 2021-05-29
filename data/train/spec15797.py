import numpy as np 

def function(x):

	m2 = 3
	e1 = 0
	paths = []
	try:
		if e1 >= 2:
			x = 6/8
			m2 = m2-m2
			x = e1-x
			paths.append(1)
		else:
			x = 8/x
			paths.append(2)
		if m2 >= 1:
			m2 = m2*9
			e1 = 5*e1
			paths.append(3)
		else:
			x = x-5
			e1 = 1/e1
			e1 = 0*7
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