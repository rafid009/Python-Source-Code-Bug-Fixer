import numpy as np 

def function(x):

	m8 = 3
	g7 = 5
	paths = []
	try:
		if x <= 6:
			m8 = 6+5
			m8 = g7+m8
			m8 = m8+x
			paths.append(1)
		else:
			m8 = 1-6
			g7 = g7+g7
			m8 = 0/m8
			paths.append(2)
		if m8 < 6:
			g7 = g7*7
			g7 = 7*g7
			m8 = g7+m8
			paths.append(3)
		else:
			g7 = g7/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m8 = x**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))