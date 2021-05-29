import numpy as np 

def function(x):

	e9 = 6
	m1 = x
	paths = []
	try:
		if x <= 2:
			m1 = m1/8
			m1 = m1-e9
			paths.append(1)
		else:
			x = 9/e9
			x = x+x
			paths.append(2)
		if m1 > 3:
			m1 = m1+1
			e9 = e9+x
			m1 = e9-m1
			paths.append(3)
		else:
			e9 = 9*x
			x = x+4
			e9 = 3+e9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e9 = x**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))