import numpy as np 

def function(x):

	e2 = 8
	m4 = x
	paths = []
	try:
		if x > 6:
			e2 = e2-e2
			x = e2-2
			m4 = m4+3
			paths.append(1)
		else:
			x = 2+x
			paths.append(2)
		if x <= 7:
			x = 0+x
			paths.append(3)
		else:
			e2 = 1-7
			x = 3+x
			x = x-3
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		e2 = m4**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))