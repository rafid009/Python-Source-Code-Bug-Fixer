import numpy as np 

def function(x):

	a2 = 6
	m6 = 2
	paths = []
	try:
		if a2 <= 0:
			m6 = 7-m6
			m6 = m6+4
			m6 = m6/m6
			paths.append(1)
		else:
			x = x-9
			m6 = m6*x
			m6 = m6/7
			paths.append(2)
		if a2 < 9:
			a2 = 5/2
			paths.append(3)
		else:
			x = x+0
			m6 = 9*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a2 = x**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))