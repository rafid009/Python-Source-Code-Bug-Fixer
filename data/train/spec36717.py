import numpy as np 

def function(x):

	m4 = x
	g1 = x
	paths = []
	try:
		if g1 < 9:
			m4 = m4+m4
			x = 4*x
			paths.append(1)
		else:
			g1 = g1-2
			x = x+5
			g1 = g1-x
			paths.append(2)
		if x <= 9:
			m4 = 4-m4
			paths.append(3)
		else:
			m4 = 0-x
			g1 = 3/g1
			x = 8-3
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		m4 = g1**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))