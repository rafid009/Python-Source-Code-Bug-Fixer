import numpy as np 

def function(x):

	x9 = 8
	m6 = 6
	paths = []
	try:
		if x <= 7:
			m6 = m6*3
			x9 = m6*1
			paths.append(1)
		else:
			m6 = m6+4
			m6 = 8+5
			paths.append(2)
		if x9 > 4:
			x9 = 7+x9
			paths.append(3)
		else:
			m6 = 3/9
			x = m6+5
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