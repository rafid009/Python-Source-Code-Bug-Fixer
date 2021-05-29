import numpy as np 

def function(x):

	g6 = 6
	m9 = 2
	paths = []
	try:
		if x <= 3:
			x = m9/m9
			x = 6-x
			paths.append(1)
		else:
			g6 = g6+5
			m9 = 5-m9
			g6 = x-9
			paths.append(2)
		if x >= 1:
			x = 8+5
			m9 = m9*g6
			paths.append(3)
		else:
			m9 = 5+m9
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