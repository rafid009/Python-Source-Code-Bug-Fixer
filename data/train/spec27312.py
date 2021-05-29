import numpy as np 

def function(x):

	m1 = 3
	g8 = x
	paths = []
	try:
		if g8 >= 0:
			g8 = g8/4
			g8 = g8+8
			paths.append(1)
		else:
			x = m1-g8
			paths.append(2)
		if m1 >= 6:
			g8 = x+0
			g8 = g8-3
			m1 = x+8
			paths.append(3)
		else:
			m1 = 3-m1
			x = x-5
			g8 = 0-6
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		m1 = g8**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))