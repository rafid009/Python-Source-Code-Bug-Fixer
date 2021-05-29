import numpy as np 

def function(x):

	a3 = x
	m6 = x
	paths = []
	try:
		if x >= 3:
			x = 8+2
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if a3 > 2:
			x = x*a3
			m6 = x/4
			a3 = x-1
			paths.append(3)
		else:
			x = a3/3
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