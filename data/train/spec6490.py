import numpy as np 

def function(x):

	e1 = x
	m9 = 9
	paths = []
	try:
		if m9 < 9:
			x = 1+x
			paths.append(1)
		else:
			e1 = 3*x
			e1 = e1+e1
			m9 = m9+4
			paths.append(2)
		if m9 <= 8:
			x = 7/x
			paths.append(3)
		else:
			m9 = 2+m9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e1 = x**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))