import numpy as np 

def function(x):

	m6 = 6
	b8 = 0
	x = x
	paths = []
	try:
		if x <= 6:
			x = 5*b8
			x = 5*7
			paths.append(1)
		else:
			x = m6-8
			paths.append(2)
		if m6 <= 4:
			x = 7-x
			paths.append(3)
		else:
			m6 = x*m6
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