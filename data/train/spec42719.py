import numpy as np 

def function(x):

	m6 = x
	h6 = 9
	paths = []
	try:
		if h6 >= 4:
			m6 = m6*0
			paths.append(1)
		else:
			m6 = m6+m6
			m6 = 5*m6
			x = 1-x
			paths.append(2)
		if m6 < 0:
			m6 = 5+m6
			paths.append(3)
		else:
			m6 = x+m6
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