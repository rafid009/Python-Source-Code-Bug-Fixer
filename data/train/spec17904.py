import numpy as np 

def function(x):

	y6 = x
	m6 = 5
	paths = []
	try:
		if m6 >= 7:
			m6 = m6*9
			m6 = 7+m6
			paths.append(1)
		else:
			x = 4/x
			y6 = y6-6
			paths.append(2)
		if m6 < 6:
			y6 = 9-y6
			paths.append(3)
		else:
			x = y6/2
			y6 = y6-x
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