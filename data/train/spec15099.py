import numpy as np 

def function(x):

	a1 = 2
	m6 = x
	paths = []
	try:
		if x >= 3:
			a1 = 5-a1
			m6 = x/m6
			x = 8/m6
			paths.append(1)
		else:
			x = 1/a1
			m6 = a1+m6
			m6 = 7/m6
			paths.append(2)
		if x < 2:
			a1 = a1-x
			paths.append(3)
		else:
			m6 = a1+2
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		m6 = m6**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))