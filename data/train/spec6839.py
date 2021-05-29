import numpy as np 

def function(x):

	m4 = 3
	a3 = 1
	paths = []
	try:
		if m4 > 3:
			a3 = x*a3
			paths.append(1)
		else:
			m4 = 1-6
			a3 = a3+2
			a3 = 9*7
			paths.append(2)
		if x >= 2:
			a3 = x+5
			paths.append(3)
		else:
			a3 = a3-8
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		m4 = m4**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))