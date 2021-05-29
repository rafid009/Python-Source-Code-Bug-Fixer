import numpy as np 

def function(x):

	e9 = 0
	m1 = 9
	paths = []
	try:
		if e9 >= 1:
			m1 = 1-m1
			m1 = m1+3
			e9 = e9*4
			paths.append(1)
		else:
			e9 = 6+m1
			paths.append(2)
		if m1 >= 9:
			m1 = 0/x
			m1 = 2/3
			paths.append(3)
		else:
			e9 = x+e9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m1 = x**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))