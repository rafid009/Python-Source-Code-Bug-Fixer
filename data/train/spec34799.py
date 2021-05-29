import numpy as np 

def function(x):

	e5 = 5
	m9 = x
	paths = []
	try:
		if x > 1:
			e5 = e5*8
			paths.append(1)
		else:
			e5 = 3/x
			x = 9*x
			paths.append(2)
		if x <= 1:
			m9 = 5-m9
			e5 = 6/9
			e5 = m9-m9
			paths.append(3)
		else:
			m9 = 9/8
			e5 = 7+9
			m9 = m9-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e5 = x**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))