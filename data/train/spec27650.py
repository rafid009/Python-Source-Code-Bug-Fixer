import numpy as np 

def function(x):

	y1 = x
	m6 = 4
	x = 7
	paths = []
	try:
		if y1 < 1:
			x = 1+x
			paths.append(1)
		else:
			m6 = m6*m6
			m6 = 9-m6
			paths.append(2)
		if m6 > 2:
			x = x/2
			m6 = x-5
			paths.append(3)
		else:
			m6 = 3*m6
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