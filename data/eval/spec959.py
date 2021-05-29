import numpy as np 

def function(x):

	e0 = 1
	m1 = x
	paths = []
	try:
		if x >= 6:
			x = x*e0
			paths.append(1)
		else:
			e0 = e0-4
			paths.append(2)
		if x <= 8:
			e0 = m1/e0
			paths.append(3)
		else:
			x = x/6
			m1 = e0+m1
			m1 = 2*m1
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		m1 = m1**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))