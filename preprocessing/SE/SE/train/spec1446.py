import numpy as np 

def function(x):

	m6 = 5
	y7 = 1
	paths = []
	try:
		if m6 >= 6:
			m6 = m6/7
			x = x*5
			m6 = m6/m6
			paths.append(1)
		else:
			y7 = 6*y7
			paths.append(2)
		if m6 > 6:
			y7 = 7*1
			x = y7+x
			paths.append(3)
		else:
			m6 = m6*x
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