import numpy as np 

def function(x):

	m9 = x
	g0 = 1
	paths = []
	try:
		if x > 0:
			m9 = 9/g0
			paths.append(1)
		else:
			g0 = m9*g0
			paths.append(2)
		if x >= 1:
			m9 = 1+4
			paths.append(3)
		else:
			m9 = g0-m9
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		m9 = m9**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))